"""Generated from Smithy shape ``com.amazonaws.iotsitewise#InterfaceSummary``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.id


class InterfaceSummary(TypedDict):
    interface_asset_model_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the interface asset model that contains this property.</p>"""
    interface_asset_model_property_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the property in the interface asset model that corresponds to this property.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InterfaceSummary) -> dict:
    out: dict = {}
    out["interfaceAssetModelId"] = value["interface_asset_model_id"]
    out["interfaceAssetModelPropertyId"] = value["interface_asset_model_property_id"]
    return out


def deserialize_json(data: dict) -> InterfaceSummary:
    out: InterfaceSummary = {}  # type: ignore[typeddict-item]
    if "interfaceAssetModelId" in data:
        out["interface_asset_model_id"] = data["interfaceAssetModelId"]
    else:
        raise DeserializationError("InterfaceSummary.interface_asset_model_id required")
    if "interfaceAssetModelPropertyId" in data:
        out["interface_asset_model_property_id"] = data["interfaceAssetModelPropertyId"]
    else:
        raise DeserializationError(
            "InterfaceSummary.interface_asset_model_property_id required"
        )
    return out
