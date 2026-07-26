"""Generated from Smithy shape ``com.amazonaws.devopsagent#AssetFileSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_devops_agent.types.asset_file_path


class AssetFileSummary(TypedDict, closed=True):
    path: "capo_devops_agent.types.asset_file_path.AssetFilePath"
    """<p>The path of this file within the asset</p>"""
    metadata: NotRequired["object"]
    """<p>The metadata for this file</p>"""
    version: "int"
    """<p>The asset version this file belongs to</p>"""
    created_at: "datetime.datetime"
    """<p>Timestamp when this file was created</p>"""
    updated_at: "datetime.datetime"
    """<p>Timestamp when this file was last updated</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetFileSummary) -> dict:
    out: dict = {}
    out["path"] = value["path"]
    if "metadata" in value:
        out["metadata"] = value["metadata"]
    out["version"] = value["version"]
    import capo_devops_agent.types._prelude.timestamp

    out["createdAt"] = capo_devops_agent.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_devops_agent.types._prelude.timestamp

    out["updatedAt"] = capo_devops_agent.types._prelude.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> AssetFileSummary:
    out: AssetFileSummary = {}  # type: ignore[typeddict-item]
    if "path" in data:
        out["path"] = data["path"]
    else:
        raise DeserializationError("AssetFileSummary.path required")
    if "metadata" in data:
        out["metadata"] = data["metadata"]
    if "version" in data:
        out["version"] = data["version"]
    else:
        raise DeserializationError("AssetFileSummary.version required")
    if "createdAt" in data:
        import capo_devops_agent.types._prelude.timestamp

        out["created_at"] = capo_devops_agent.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("AssetFileSummary.created_at required")
    if "updatedAt" in data:
        import capo_devops_agent.types._prelude.timestamp

        out["updated_at"] = capo_devops_agent.types._prelude.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("AssetFileSummary.updated_at required")
    return out
