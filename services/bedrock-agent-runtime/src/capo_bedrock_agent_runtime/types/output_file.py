"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#OutputFile``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.file_body
    import capo_bedrock_agent_runtime.types.mime_type


class OutputFile(TypedDict, closed=True):
    name: NotRequired["str"]
    """<p>The name of the file containing response from code interpreter.</p>"""
    type: NotRequired["capo_bedrock_agent_runtime.types.mime_type.MimeType"]
    """<p>The type of file that contains response from the code interpreter.</p>"""
    bytes: NotRequired["capo_bedrock_agent_runtime.types.file_body.FileBody"]
    """<p>The byte count of files that contains response from code interpreter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OutputFile) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "type" in value:
        out["type"] = value["type"]
    if "bytes" in value:
        import capo_bedrock_agent_runtime.types.file_body

        out["bytes"] = capo_bedrock_agent_runtime.types.file_body.serialize_json(
            value["bytes"]
        )
    return out


def deserialize_json(data: dict) -> OutputFile:
    out: OutputFile = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("bytes") is not None:
        import capo_bedrock_agent_runtime.types.file_body

        out["bytes"] = capo_bedrock_agent_runtime.types.file_body.deserialize_json(
            data["bytes"]
        )
    return out
