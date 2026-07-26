"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeAssetModelInterfaceRelationshipResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.hierarchy_mappings
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.property_mappings


class DescribeAssetModelInterfaceRelationshipResponse(TypedDict, closed=True):
    asset_model_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the asset model.</p>"""
    interface_asset_model_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the interface asset model.</p>"""
    property_mappings: "capo_iotsitewise.types.property_mappings.PropertyMappings"
    """<p>A list of property mappings between the interface asset model and the asset model where the interface is applied.</p>"""
    hierarchy_mappings: "capo_iotsitewise.types.hierarchy_mappings.HierarchyMappings"
    """<p>A list of hierarchy mappings between the interface asset model and the asset model where the interface is applied.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAssetModelInterfaceRelationshipResponse) -> dict:
    out: dict = {}
    out["assetModelId"] = value["asset_model_id"]
    out["interfaceAssetModelId"] = value["interface_asset_model_id"]
    import capo_iotsitewise.types.property_mappings

    out["propertyMappings"] = capo_iotsitewise.types.property_mappings.serialize_json(
        value["property_mappings"]
    )
    import capo_iotsitewise.types.hierarchy_mappings

    out["hierarchyMappings"] = capo_iotsitewise.types.hierarchy_mappings.serialize_json(
        value["hierarchy_mappings"]
    )
    return out


def deserialize_json(data: dict) -> DescribeAssetModelInterfaceRelationshipResponse:
    out: DescribeAssetModelInterfaceRelationshipResponse = {}  # type: ignore[typeddict-item]
    if "assetModelId" in data:
        out["asset_model_id"] = data["assetModelId"]
    else:
        raise DeserializationError(
            "DescribeAssetModelInterfaceRelationshipResponse.asset_model_id required"
        )
    if "interfaceAssetModelId" in data:
        out["interface_asset_model_id"] = data["interfaceAssetModelId"]
    else:
        raise DeserializationError(
            "DescribeAssetModelInterfaceRelationshipResponse.interface_asset_model_id required"
        )
    if "propertyMappings" in data:
        import capo_iotsitewise.types.property_mappings

        out["property_mappings"] = (
            capo_iotsitewise.types.property_mappings.deserialize_json(
                data["propertyMappings"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeAssetModelInterfaceRelationshipResponse.property_mappings required"
        )
    if "hierarchyMappings" in data:
        import capo_iotsitewise.types.hierarchy_mappings

        out["hierarchy_mappings"] = (
            capo_iotsitewise.types.hierarchy_mappings.deserialize_json(
                data["hierarchyMappings"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeAssetModelInterfaceRelationshipResponse.hierarchy_mappings required"
        )
    return out
