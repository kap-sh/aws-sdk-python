"""Generated from Smithy shape ``com.amazonaws.iotsitewise#PropertyMapping``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.custom_id


class PropertyMapping(TypedDict):
    asset_model_property_id: "aws_sdk_iotsitewise.types.custom_id.CustomID"
    """<p>The ID of the property in the asset model where the interface is applied.</p>"""
    interface_asset_model_property_id: "aws_sdk_iotsitewise.types.custom_id.CustomID"
    """<p>The ID of the property in the interface asset model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PropertyMapping) -> dict:
    out: dict = {}
    out["assetModelPropertyId"] = value["asset_model_property_id"]
    out["interfaceAssetModelPropertyId"] = value["interface_asset_model_property_id"]
    return out


def deserialize_json(data: dict) -> PropertyMapping:
    out: PropertyMapping = {}  # type: ignore[typeddict-item]
    if "assetModelPropertyId" in data:
        out["asset_model_property_id"] = data["assetModelPropertyId"]
    else:
        raise DeserializationError("PropertyMapping.asset_model_property_id required")
    if "interfaceAssetModelPropertyId" in data:
        out["interface_asset_model_property_id"] = data["interfaceAssetModelPropertyId"]
    else:
        raise DeserializationError(
            "PropertyMapping.interface_asset_model_property_id required"
        )
    return out
