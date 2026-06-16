# Skills & Tool Reference (read-only)

## File reading (lean context)

Files added via /add are NOT loaded into chat as full text. Read them on demand.

- Read exact contents before editing:
  `mcp2cli @leanctx ctx-read --path <ABSOLUTE_PATH> --mode full`
- Read a compressed/auto view (default, cheap):
  `mcp2cli @leanctx ctx-read --path <ABSOLUTE_PATH>`
- Analyze a file in-sandbox without loading it (counts, structure, aggregation):
  `mcp2cli @context-mode ctx-execute-file --path <PATH> --language javascript --code "<code>"`

All run in ````bash` blocks; output returns automatically. Use `--mode full` only right before editing.

## mcp2cli baked tools

Invoke with `mcp2cli @<name> <command> [args]`. `mcp2cli @<name> --list` shows commands.

### leanctx (lean-ctx) — primary file/code tools
- `ctx-read --path <P> [--mode full|auto|map|signatures] [--fresh]` — read a file (cached, compressed). Prefer over cat/head/tail.
- `ctx-search "<regex>"` — regex code search (.gitignore-aware). Prefer over grep/rg.
- `ctx-tree <dir>` — directory tree with counts.
- `ctx-overview` — task-relevant project map (use at session start).
- `ctx-shell <cmd>` — run a shell command with compressed output (builds/tests/logs).
- `ctx-edit` — search-and-replace edit when Edit is unavailable.
- `ctx-graph` — deps, usages, impact/blast-radius.
- `ctx-semantic-search "<q>"` — hybrid BM25+embeddings concept search.

### context-mode — sandbox execution & knowledge
- `ctx-execute-file --path <P> --language javascript --code "<code>"` — run code over FILE_CONTENT (bytes stay in sandbox).
- `ctx-execute --language <lang> --code "<code>"` — run sandboxed code.
- `ctx-search "<q>"` — search the persistent knowledge base.
- `ctx-index --path <P|dir> --source <label>` — index content for recall.
- `ctx-batch-execute` — run many commands, query results inline.

### codegraph / semble / code-review-graph
See `mcp2cli @<name> --list`. codegraph for call-graph/impact; semble for semantic code search.
