"""Generated from Smithy shape ``com.amazonaws.devopsagent#AssetVersionMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import datetime


class AssetVersionMetadata(TypedDict):
    version: "int"
    """<p>The version number of this asset</p>"""
    created_at: "datetime.datetime"
    """<p>Timestamp when this asset version was created</p>"""
    updated_at: "datetime.datetime"
    """<p>Timestamp when this asset version was last updated</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetVersionMetadata) -> dict:
    out: dict = {}
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


def deserialize_json(data: dict) -> AssetVersionMetadata:
    out: AssetVersionMetadata = {}  # type: ignore[typeddict-item]
    if "version" in data:
        out["version"] = data["version"]
    else:
        raise DeserializationError("AssetVersionMetadata.version required")
    if "createdAt" in data:
        import aws_sdk_devops_agent.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_devops_agent.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("AssetVersionMetadata.created_at required")
    if "updatedAt" in data:
        import aws_sdk_devops_agent.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_devops_agent.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("AssetVersionMetadata.updated_at required")
    return out
