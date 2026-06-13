"""Generated from Smithy shape ``com.amazonaws.devopsagent#AssetFileContent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.asset_file_body
    import aws_sdk_devops_agent.types.asset_file_path


class AssetFileContent(TypedDict):
    path: "aws_sdk_devops_agent.types.asset_file_path.AssetFilePath"
    """<p>The path of the file within the asset</p>"""
    body: "aws_sdk_devops_agent.types.asset_file_body.AssetFileBody"
    """<p>The file content</p>"""
    metadata: NotRequired["object"]
    """<p>Optional metadata for this file</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetFileContent) -> dict:
    out: dict = {}
    out["path"] = value["path"]
    import aws_sdk_devops_agent.types.asset_file_body

    out["body"] = aws_sdk_devops_agent.types.asset_file_body.serialize_json(
        value["body"]
    )
    if "metadata" in value:
        out["metadata"] = value["metadata"]
    return out


def deserialize_json(data: dict) -> AssetFileContent:
    out: AssetFileContent = {}  # type: ignore[typeddict-item]
    if "path" in data:
        out["path"] = data["path"]
    else:
        raise DeserializationError("AssetFileContent.path required")
    if "body" in data:
        import aws_sdk_devops_agent.types.asset_file_body

        out["body"] = aws_sdk_devops_agent.types.asset_file_body.deserialize_json(
            data["body"]
        )
    else:
        raise DeserializationError("AssetFileContent.body required")
    if "metadata" in data:
        out["metadata"] = data["metadata"]
    return out
