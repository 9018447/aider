shell_cmd_prompt = """
4. *Concisely* suggest any shell commands the user might want to run in ```bash blocks.

Just suggest shell commands this way, not example code.
Only suggest complete shell commands that are ready to execute, without placeholders.
Only suggest at most a few shell commands at a time, not more than 1-3, one per line.
Do not suggest multi-line shell commands.
All shell commands will run from the root directory of the user's project.

Use the appropriate shell based on the user's system info:
{platform}
Examples of when to suggest shell commands:

- If you changed a self-contained html file, suggest an OS-appropriate command to open a browser to view it to see the updated content.
- If you changed a CLI program, suggest the command to run it to see the new behavior.
- If you added a test, suggest how to run it with the testing tool used by the project.
- Suggest OS-appropriate commands to delete or rename files/directories, or other file system operations.
- If your code changes add new dependencies, suggest the command to install them.
- Etc.
"""  # noqa

no_shell_cmd_prompt = """
Keep in mind these details about the user's platform and environment:
{platform}
"""  # noqa

shell_cmd_reminder = """
Examples of when to suggest shell commands:

- If you changed a self-contained html file, suggest an OS-appropriate command to open a browser to view it to see the updated content.
- If you changed a CLI program, suggest the command to run it to see the new behavior.
- If you added a test, suggest how to run it with the testing tool used by the project.
- Suggest OS-appropriate commands to delete or rename files/directories, or other file system operations.
- If your code changes add new dependencies, suggest the command to install them.
- Etc.

"""  # noqa
tool_cmd_prompt = """
4. You have tools available via shell commands in ```bash blocks.

Tool commands you run in ```bash blocks will be EXECUTED AUTOMATICALLY — no user confirmation needed, EXCEPT as noted below.
Use tools proactively to:
- ANALYZE a file without loading it (counts, structure, aggregation): mcp2cli @context-mode ctx-execute-file --path <PATH> --language javascript --code "<code>"
- Search and explore code before editing
- Verify your changes (run tests, linters)
- Look up documentation or APIs
- READ the complete contents of a file that is NOT listed under "Editable files": mcp2cli @leanctx ctx-read --path <ABSOLUTE_PATH> --mode full
  NOTE: full-file reads require explicit user approval before they run. Prefer context-mode analysis whenever possible.
CRITICAL: Only the files listed under "Editable files" below are actually loaded into the conversation. A file name appearing in chat text is NOT automatically loaded.
Do not read files that are already listed under "Editable files".
Avoid reading the same file repeatedly; cache the result in your reasoning.
If you need to edit a file that is not listed under "Editable files", ask the user to add it with `/add <file>`.
Refer to the SKILL.md file in the read-only context for exact tool command syntax.

All shell commands run from the root directory of the user's project.
Platform: {platform}
"""  # noqa

tool_cmd_reminder = """
Remember: shell commands in ```bash blocks are auto-executed. Use them freely to call tools.
"""  # noqa
