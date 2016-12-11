#!/usr/bin/env python
import os
import unittest

import frontmatter


recipe_files = []
for root, dirs, files in os.walk("baking"):
    recipe_files += [os.path.join(root, name) for name in files]

recipe_headers = []
for filename in recipe_files:
    print(filename)
    markdown = frontmatter.load(filename)
    recipe_headers.append((filename, set(markdown.keys())))


class RecipesTestCase(unittest.TestCase):
    def assertMetaIn(self, key, meta, filename):
            self.assertIn(key, meta, "{}".format(filename))

    def test_all_recipes__has_name(self):
        for file_name, meta in recipe_headers:
            self.assertMetaIn("name", meta, filename)

    def test_all_recipes__has_source(self):
        for file_name, meta in recipe_headers:
            if "source" not in meta and "source_url" not in meta:
                self.fail("{} does not have a source.".format(filename))

    def test_all_recipes__has_time(self):
        for file_name, meta in recipe_headers:
            self.assertMetaIn("time", meta, filename)
            # TODO time format


if __name__ == "__main__":
    unittest.main()
