"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#CodeInterpreterInvocationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.files


class CodeInterpreterInvocationInput(TypedDict, closed=True):
    code: NotRequired["str"]
    """<p>The code for the code interpreter to use.</p>"""
    files: NotRequired["capo_bedrock_agent_runtime.types.files.Files"]
    """<p>Files that are uploaded for code interpreter to use.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeInterpreterInvocationInput) -> dict:
    out: dict = {}
    if "code" in value:
        out["code"] = value["code"]
    if "files" in value:
        import capo_bedrock_agent_runtime.types.files

        out["files"] = capo_bedrock_agent_runtime.types.files.serialize_json(
            value["files"]
        )
    return out


def deserialize_json(data: dict) -> CodeInterpreterInvocationInput:
    out: CodeInterpreterInvocationInput = {}  # type: ignore[typeddict-item]
    if data.get("code") is not None:
        out["code"] = data["code"]
    if data.get("files") is not None:
        import capo_bedrock_agent_runtime.types.files

        out["files"] = capo_bedrock_agent_runtime.types.files.deserialize_json(
            data["files"]
        )
    return out
