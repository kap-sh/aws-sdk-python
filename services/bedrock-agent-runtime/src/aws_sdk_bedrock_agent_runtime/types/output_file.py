"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#OutputFile``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.file_body
    import aws_sdk_bedrock_agent_runtime.types.mime_type


class OutputFile(TypedDict):
    name: NotRequired["str"]
    """<p>The name of the file containing response from code interpreter.</p>"""
    type: NotRequired["aws_sdk_bedrock_agent_runtime.types.mime_type.MimeType"]
    """<p>The type of file that contains response from the code interpreter.</p>"""
    bytes: NotRequired["aws_sdk_bedrock_agent_runtime.types.file_body.FileBody"]
    """<p>The byte count of files that contains response from code interpreter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OutputFile) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "type" in value:
        out["type"] = value["type"]
    if "bytes" in value:
        import aws_sdk_bedrock_agent_runtime.types.file_body

        out["bytes"] = aws_sdk_bedrock_agent_runtime.types.file_body.serialize_json(
            value["bytes"]
        )
    return out


def deserialize_json(data: dict) -> OutputFile:
    out: OutputFile = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "type" in data:
        out["type"] = data["type"]
    if "bytes" in data:
        import aws_sdk_bedrock_agent_runtime.types.file_body

        out["bytes"] = aws_sdk_bedrock_agent_runtime.types.file_body.deserialize_json(
            data["bytes"]
        )
    return out
