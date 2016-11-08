#!/usr/bin/env python
import os
import unittest

import frontmatter


baking_recipe_files = []
for root, dirs, files in os.walk("baking"):
    baking_recipe_files += [os.path.join(root, name) for name in files]

recipe_files = baking_recipe_files

recipe_headers = []
for filename in recipe_files:
    print(filename)
    markdown = frontmatter.load(filename)
    recipe_headers.append((filename, set(markdown.keys())))


class RecipesTestCase(unittest.TestCase):
    def test_all_recipes__has_name(self):
        for file_name, meta in recipe_headers:
            self.assertIn("name", meta)

    def test_all_recipes__has_source(self):
        for file_name, meta in recipe_headers:
            self.assertIn("source_url", meta)

    def test_all_recipes__has_time(self):
        for file_name, meta in recipe_headers:
            self.assertIn("time", meta)
            # TODO time format


if __name__ == "__main__":
    unittest.main()
