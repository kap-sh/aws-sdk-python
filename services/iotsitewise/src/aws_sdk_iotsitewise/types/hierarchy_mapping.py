"""Generated from Smithy shape ``com.amazonaws.iotsitewise#HierarchyMapping``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.id


class HierarchyMapping(TypedDict):
    asset_model_hierarchy_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the hierarchy in the asset model where the interface is applied.</p>"""
    interface_asset_model_hierarchy_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the hierarchy in the interface asset model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HierarchyMapping) -> dict:
    out: dict = {}
    out["assetModelHierarchyId"] = value["asset_model_hierarchy_id"]
    out["interfaceAssetModelHierarchyId"] = value["interface_asset_model_hierarchy_id"]
    return out


def deserialize_json(data: dict) -> HierarchyMapping:
    out: HierarchyMapping = {}  # type: ignore[typeddict-item]
    if "assetModelHierarchyId" in data:
        out["asset_model_hierarchy_id"] = data["assetModelHierarchyId"]
    else:
        raise DeserializationError("HierarchyMapping.asset_model_hierarchy_id required")
    if "interfaceAssetModelHierarchyId" in data:
        out["interface_asset_model_hierarchy_id"] = data[
            "interfaceAssetModelHierarchyId"
        ]
    else:
        raise DeserializationError(
            "HierarchyMapping.interface_asset_model_hierarchy_id required"
        )
    return out
