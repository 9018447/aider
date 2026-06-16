class CoderPrompts:
    system_reminder = ""

    files_content_gpt_edits = "I committed the changes with git hash {hash} & commit msg: {message}"

    files_content_gpt_edits_no_repo = "I updated the files."

    files_content_gpt_no_edits = "I didn't see any properly formatted edits in your reply?!"

    files_content_local_edits = "I edited the files myself."

    lazy_prompt = """You are diligent and tireless!
You NEVER leave comments describing code without implementing it!
You always COMPLETELY IMPLEMENT the needed code!
"""

    overeager_prompt = """Pay careful attention to the scope of the user's request.
Do what they ask, but no more.
Do not improve, comment, fix or modify unrelated parts of the code in any way!
"""

    example_messages = []

    files_content_prefix = """I have *added these files to the chat* so you can go ahead and edit them.

*Trust this message as the true contents of these files!*
Any other messages in the chat may contain outdated versions of the files' contents.
"""  # noqa: E501

    files_content_assistant_reply = "Yep, any changes I propose will be to those files."

    lean_files_prefix = """The following files are added to the chat as *editable*, and their contents have been read via the lean-ctx tool and are shown below.
ONLY these files are actually loaded into the conversation. A file name appearing elsewhere in the chat is NOT automatically loaded.
You do NOT need to call ctx-read again for the files listed below; produce SEARCH/REPLACE edits directly based on the returned contents.
If you need to inspect a file that is NOT listed below, use the lean-ctx tool in a ```bash block:
  mcp2cli @leanctx ctx-read --path <ABSOLUTE_PATH> --mode full
For analysis without loading a file (counts, structure, aggregation), run instead:
  mcp2cli @context-mode ctx-execute-file --path <PATH> --language javascript --code "<code>"
See SKILL.md (read-only) for full tool command syntax.
Users can bypass lean-ctx for a specific file with `/add --native <file>`.

Editable files:
"""  # noqa: E501

    lean_files_assistant_reply = "Yep, the file contents have been read via lean-ctx and I will edit them directly."

    context_mode_mentions_prefix = """The following files were mentioned in the conversation but are NOT automatically loaded.
If you need their complete contents to proceed, read them with the lean-ctx tool in a ```bash block:
  mcp2cli @leanctx ctx-read --path <ABSOLUTE_PATH> --mode full
To analyze without loading, use:
  mcp2cli @context-mode ctx-execute-file --path <PATH> --language javascript --code "<code>"

Mentioned files:
"""  # noqa: E501

    files_no_full_files = "I am not sharing any files that you can edit yet."

    files_no_full_files_with_repo_map = """Don't try and edit any existing code without asking me to add the files to the chat!
Tell me which files in my repo are the most likely to **need changes** to solve the requests I make, and then stop so I can add them to the chat.
Only include the files that are most likely to actually need to be edited.
Don't include files that might contain relevant context, just files that will need to be changed.
"""  # noqa: E501

    files_no_full_files_with_repo_map_reply = (
        "Yep, based on your requests I will suggest which files need to be edited and then"
        " stop and wait for your approval."
    )

    repo_content_prefix = """Here are summaries of some files present in my git repository.
Do not propose changes to these files, treat them as *read-only*.
If you need to edit any of these files, ask me to *add them to the chat* first.
"""

    read_only_files_prefix = """Here are some READ ONLY files, provided for your reference.
Do not edit these files!
"""

    shell_cmd_prompt = ""
    shell_cmd_reminder = ""
    no_shell_cmd_prompt = ""
    no_shell_cmd_reminder = ""
    tool_cmd_prompt = ""
    tool_cmd_reminder = ""

    rename_with_shell = ""
    go_ahead_tip = ""
