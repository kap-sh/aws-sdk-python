"""Generated from Smithy shape ``com.amazonaws.devopsagent#AssetTypeSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.asset_type


class AssetTypeSummary(TypedDict, closed=True):
    asset_type: "capo_devops_agent.types.asset_type.AssetType"
    """<p>The asset type identifier</p>"""
    description: "str"
    """<p>A description of the asset type</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetTypeSummary) -> dict:
    out: dict = {}
    out["assetType"] = value["asset_type"]
    out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> AssetTypeSummary:
    out: AssetTypeSummary = {}  # type: ignore[typeddict-item]
    if "assetType" in data:
        out["asset_type"] = data["assetType"]
    else:
        raise DeserializationError("AssetTypeSummary.asset_type required")
    if "description" in data:
        out["description"] = data["description"]
    else:
        raise DeserializationError("AssetTypeSummary.description required")
    return out
