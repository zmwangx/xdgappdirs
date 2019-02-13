import sys
import unittest
import xdgappdirs

if sys.version_info[0] < 3:
    STRING_TYPE = basestring
    import pathlib2 as pathlib
else:
    STRING_TYPE = str
    import pathlib


class Test_AppDir(unittest.TestCase):
    def test_metadata(self):
        self.assertTrue(hasattr(xdgappdirs, "__version__"))
        self.assertTrue(hasattr(xdgappdirs, "__version_info__"))

    def test_helpers_defaults(self):
        self.assertIsInstance(
            xdgappdirs.user_data_dir('MyApp', 'MyCompany'), STRING_TYPE)
        self.assertIsInstance(
            xdgappdirs.site_data_dir('MyApp', 'MyCompany'), STRING_TYPE)
        self.assertIsInstance(
            xdgappdirs.user_cache_dir('MyApp', 'MyCompany'), STRING_TYPE)
        self.assertIsInstance(
            xdgappdirs.user_state_dir('MyApp', 'MyCompany'), STRING_TYPE)
        self.assertIsInstance(
            xdgappdirs.user_log_dir('MyApp', 'MyCompany'), STRING_TYPE)

    def test_helpers_paths(self):
        self.assertIsInstance(
            xdgappdirs.user_data_dir('MyApp', 'MyCompany', as_path=True), pathlib.Path)
        self.assertIsInstance(
            xdgappdirs.site_data_dir('MyApp', 'MyCompany', as_path=True), pathlib.Path)
        self.assertIsInstance(
            xdgappdirs.user_cache_dir('MyApp', 'MyCompany', as_path=True), pathlib.Path)
        self.assertIsInstance(
            xdgappdirs.user_state_dir('MyApp', 'MyCompany', as_path=True), pathlib.Path)
        self.assertIsInstance(
            xdgappdirs.user_log_dir('MyApp', 'MyCompany', as_path=True), pathlib.Path)


    def test_dirs(self):
        dirs = xdgappdirs.AppDirs('MyApp', 'MyCompany', version='1.0')
        self.assertIsInstance(dirs.user_data_dir, STRING_TYPE)
        self.assertIsInstance(dirs.site_data_dir, STRING_TYPE)
        self.assertIsInstance(dirs.user_cache_dir, STRING_TYPE)
        self.assertIsInstance(dirs.user_state_dir, STRING_TYPE)
        self.assertIsInstance(dirs.user_log_dir, STRING_TYPE)

if __name__ == "__main__":
    unittest.main()
