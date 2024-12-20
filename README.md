 # UV Python Scripts Collection

 This is a collection of Python scripts that are self-contained and can be run from the command line using the `uv run` command. The user don't have to take any extra steps to install any of the dependencies that the script need. That’s because each script starts with this magic comment:

```python
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "click",
#     "urllib3",
# ]
# ///
```

This is an example of inline script dependencies, a feature described in [PEP 723](https://peps.python.org/pep-0723/) and implemented by `uv run`. Running the script causes uv to create a temporary virtual environment with those dependencies installed, a process that takes just a few milliseconds once the uv cache has been populated. This also works if the script is specified by a URL. Anyone with uv installed can run the following command:

```bash
uv run ...
```

## Description

- [fetch_yt_subs/fetch_subs.py](fetch_yt_subs/fetch_subs.py): Fetch subtitles from a YouTube video.