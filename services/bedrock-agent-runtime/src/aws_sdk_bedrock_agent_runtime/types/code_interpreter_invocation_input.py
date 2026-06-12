"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#CodeInterpreterInvocationInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.files

class CodeInterpreterInvocationInput(TypedDict):
    code: NotRequired["str"]
    """<p>The code for the code interpreter to use.</p>"""
    files: NotRequired["aws_sdk_bedrock_agent_runtime.types.files.Files"]
    """<p>Files that are uploaded for code interpreter to use.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CodeInterpreterInvocationInput) -> dict:
    out: dict = {}
    if "code" in value:
        out["code"] = value["code"]
    if "files" in value:
        import aws_sdk_bedrock_agent_runtime.types.files
        out["files"] = aws_sdk_bedrock_agent_runtime.types.files.serialize_json(value["files"])
    return out


def deserialize_json(data: dict) -> CodeInterpreterInvocationInput:
    out: CodeInterpreterInvocationInput = {}  # type: ignore[typeddict-item]
    if "code" in data:
        out["code"] = data["code"]
    if "files" in data:
        import aws_sdk_bedrock_agent_runtime.types.files
        out["files"] = aws_sdk_bedrock_agent_runtime.types.files.deserialize_json(data["files"])
    return out