Using UV with Render:

```
pip install uv
uv pip compile requirements.in --universal --output-file requirements.txt
uv init
uv add -r requirements.txt
```

build command should be `uv sync`. uv will be auto-installed if a `uv.lock` file exists. `uv add` creates a `uv.lock` file by default.