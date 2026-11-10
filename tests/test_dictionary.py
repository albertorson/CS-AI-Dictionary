import copy
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import build_extended_dictionary as ext
import build_simple_dictionary as simple


class DictionaryTests(unittest.TestCase):
    def test_community_growth_and_both_renderers(self):
        baseline, _ = ext.load_entries()
        item = json.loads((ext.ROOT / 'examples/entry.jsonl').read_text(encoding='utf-8'))
        with tempfile.TemporaryDirectory() as folder:
            Path(folder, 'arbitrary_name.jsonl').write_text(json.dumps(item), encoding='utf-8')
            with patch.object(ext, 'COMMUNITY_DIR', Path(folder)):
                entries, _ = ext.load_entries()
                self.assertEqual(len(entries), len(baseline) + 1)
                ext.validate_entries(entries)
                self.assertEqual(len(simple.load_entries()), len(entries))
                simple.verify([simple.render_line(e) for e in entries])
                self.assertEqual(len([ext.source_line(e) for e in entries]), len(entries))

    def test_duplicate_rejected(self):
        entries, _ = ext.load_entries()
        duplicate = copy.deepcopy(entries[0])
        duplicate['word'] = '  ' + duplicate['word'].upper() + '  '
        with self.assertRaises(ValueError):
            ext.validate_entries(entries + [duplicate])

    def test_missing_field_and_empty_rejected(self):
        entries, _ = ext.load_entries()
        item = copy.deepcopy(entries[0])
        del item['definition']
        with self.assertRaises(ValueError):
            ext.validate_entries([item])
        with self.assertRaises(ValueError):
            ext.validate_entries([])


if __name__ == '__main__':
    unittest.main()
