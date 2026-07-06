"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetModelPropertySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.asset_model_property_path
    import aws_sdk_iotsitewise.types.external_id
    import aws_sdk_iotsitewise.types.id
    import aws_sdk_iotsitewise.types.interface_summaries
    import aws_sdk_iotsitewise.types.name
    import aws_sdk_iotsitewise.types.property_data_type
    import aws_sdk_iotsitewise.types.property_type
    import aws_sdk_iotsitewise.types.property_unit


class AssetModelPropertySummary(TypedDict, closed=True):
    id: NotRequired["aws_sdk_iotsitewise.types.id.ID"]
    """<p>The ID of the property.</p>"""
    external_id: NotRequired["aws_sdk_iotsitewise.types.external_id.ExternalId"]
    r"""<p>The external ID of the property. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids\">Using external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    name: "aws_sdk_iotsitewise.types.name.Name"
    """<p>The name of the property.</p>"""
    data_type: "aws_sdk_iotsitewise.types.property_data_type.PropertyDataType"
    """<p>The data type of the property.</p>"""
    data_type_spec: NotRequired["aws_sdk_iotsitewise.types.name.Name"]
    """<p>The data type of the structure for this property. This parameter exists on properties that have the <code>STRUCT</code> data type.</p>"""
    unit: NotRequired["aws_sdk_iotsitewise.types.property_unit.PropertyUnit"]
    """<p>The unit (such as <code>Newtons</code> or <code>RPM</code>) of the property.</p>"""
    type: "aws_sdk_iotsitewise.types.property_type.PropertyType"
    asset_model_composite_model_id: NotRequired["aws_sdk_iotsitewise.types.id.ID"]
    """<p> The ID of the composite model that contains the asset model property. </p>"""
    path: NotRequired[
        "aws_sdk_iotsitewise.types.asset_model_property_path.AssetModelPropertyPath"
    ]
    """<p>The structured path to the property from the root of the asset model.</p>"""
    interface_summaries: NotRequired[
        "aws_sdk_iotsitewise.types.interface_summaries.InterfaceSummaries"
    ]
    """<p>A list of interface summaries that describe which interfaces this property belongs to, including the interface asset model ID and the corresponding property ID in the interface.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetModelPropertySummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    out["name"] = value["name"]
    import aws_sdk_iotsitewise.types.property_data_type

    out["dataType"] = aws_sdk_iotsitewise.types.property_data_type.serialize_json(
        value["data_type"]
    )
    if "data_type_spec" in value:
        out["dataTypeSpec"] = value["data_type_spec"]
    if "unit" in value:
        out["unit"] = value["unit"]
    import aws_sdk_iotsitewise.types.property_type

    out["type"] = aws_sdk_iotsitewise.types.property_type.serialize_json(value["type"])
    if "asset_model_composite_model_id" in value:
        out["assetModelCompositeModelId"] = value["asset_model_composite_model_id"]
    if "path" in value:
        import aws_sdk_iotsitewise.types.asset_model_property_path

        out["path"] = (
            aws_sdk_iotsitewise.types.asset_model_property_path.serialize_json(
                value["path"]
            )
        )
    if "interface_summaries" in value:
        import aws_sdk_iotsitewise.types.interface_summaries

        out["interfaceSummaries"] = (
            aws_sdk_iotsitewise.types.interface_summaries.serialize_json(
                value["interface_summaries"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssetModelPropertySummary:
    out: AssetModelPropertySummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "externalId" in data:
        out["external_id"] = data["externalId"]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AssetModelPropertySummary.name required")
    if "dataType" in data:
        import aws_sdk_iotsitewise.types.property_data_type

        out["data_type"] = (
            aws_sdk_iotsitewise.types.property_data_type.deserialize_json(
                data["dataType"]
            )
        )
    else:
        raise DeserializationError("AssetModelPropertySummary.data_type required")
    if "dataTypeSpec" in data:
        out["data_type_spec"] = data["dataTypeSpec"]
    if "unit" in data:
        out["unit"] = data["unit"]
    if "type" in data:
        import aws_sdk_iotsitewise.types.property_type

        out["type"] = aws_sdk_iotsitewise.types.property_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("AssetModelPropertySummary.type required")
    if "assetModelCompositeModelId" in data:
        out["asset_model_composite_model_id"] = data["assetModelCompositeModelId"]
    if "path" in data:
        import aws_sdk_iotsitewise.types.asset_model_property_path

        out["path"] = (
            aws_sdk_iotsitewise.types.asset_model_property_path.deserialize_json(
                data["path"]
            )
        )
    if "interfaceSummaries" in data:
        import aws_sdk_iotsitewise.types.interface_summaries

        out["interface_summaries"] = (
            aws_sdk_iotsitewise.types.interface_summaries.deserialize_json(
                data["interfaceSummaries"]
            )
        )
    return out
