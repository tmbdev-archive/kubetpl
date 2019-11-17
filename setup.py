from distutils.core import setup
import glob

files = glob.glob("kubetpl-templates/*.yaml")

setup(
    name = "kubetpl",
    version = "0",
    description = "Generate Kubernetes templates from the command line.",
    author_email = "tmbdev@gmail.com",
    data_files = [("lib/kubetpl", files )],
    scripts = ["kubetpl"],
) 
