from setuptools import setup, find_packages

# This setup.py is maintained for backward compatibility.
# The primary build configuration is in pyproject.toml

setup(
    name="site-roast",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    packages=find_packages(),
    python_requires=">=3.8",
)
