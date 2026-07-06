"""Generated from Smithy shape ``com.amazonaws.devopsagent#AssetFile``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_devops_agent.types.asset_file_body
    import aws_sdk_devops_agent.types.asset_file_path


class AssetFile(TypedDict, closed=True):
    path: "aws_sdk_devops_agent.types.asset_file_path.AssetFilePath"
    """<p>The path of this file within the asset</p>"""
    content: "aws_sdk_devops_agent.types.asset_file_body.AssetFileBody"
    """<p>The content of this file</p>"""
    metadata: NotRequired["object"]
    """<p>The metadata for this file</p>"""
    version: "int"
    """<p>The asset version this file belongs to</p>"""
    created_at: "datetime.datetime"
    """<p>Timestamp when this file was created</p>"""
    updated_at: "datetime.datetime"
    """<p>Timestamp when this file was last updated</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetFile) -> dict:
    out: dict = {}
    out["path"] = value["path"]
    import aws_sdk_devops_agent.types.asset_file_body

    out["content"] = aws_sdk_devops_agent.types.asset_file_body.serialize_json(
        value["content"]
    )
    if "metadata" in value:
        out["metadata"] = value["metadata"]
    out["version"] = value["version"]
    import aws_sdk_devops_agent.types._prelude.timestamp

    out["createdAt"] = aws_sdk_devops_agent.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_devops_agent.types._prelude.timestamp

    out["updatedAt"] = aws_sdk_devops_agent.types._prelude.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> AssetFile:
    out: AssetFile = {}  # type: ignore[typeddict-item]
    if "path" in data:
        out["path"] = data["path"]
    else:
        raise DeserializationError("AssetFile.path required")
    if "content" in data:
        import aws_sdk_devops_agent.types.asset_file_body

        out["content"] = aws_sdk_devops_agent.types.asset_file_body.deserialize_json(
            data["content"]
        )
    else:
        raise DeserializationError("AssetFile.content required")
    if "metadata" in data:
        out["metadata"] = data["metadata"]
    if "version" in data:
        out["version"] = data["version"]
    else:
        raise DeserializationError("AssetFile.version required")
    if "createdAt" in data:
        import aws_sdk_devops_agent.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_devops_agent.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("AssetFile.created_at required")
    if "updatedAt" in data:
        import aws_sdk_devops_agent.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_devops_agent.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("AssetFile.updated_at required")
    return out
