"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetModelProperty``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.asset_model_property_path
    import aws_sdk_iotsitewise.types.custom_id
    import aws_sdk_iotsitewise.types.external_id
    import aws_sdk_iotsitewise.types.name
    import aws_sdk_iotsitewise.types.property_data_type
    import aws_sdk_iotsitewise.types.property_type
    import aws_sdk_iotsitewise.types.property_unit


class AssetModelProperty(TypedDict):
    id: NotRequired["aws_sdk_iotsitewise.types.custom_id.CustomID"]
    """<p>The ID of the asset model property.</p> <ul> <li> <p>If you are callling <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetModel.html\">UpdateAssetModel</a> to create a <i>new</i> property: You can specify its ID here, if desired. IoT SiteWise automatically generates a unique ID for you, so this parameter is never required. However, if you prefer to supply your own ID instead, you can specify it here in UUID format. If you specify your own ID, it must be globally unique.</p> </li> <li> <p>If you are calling UpdateAssetModel to modify an <i>existing</i> property: This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references\">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p> </li> </ul>"""
    external_id: NotRequired["aws_sdk_iotsitewise.types.external_id.ExternalId"]
    """<p>The external ID (if any) provided in the <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAssetModel.html\">CreateAssetModel</a> or <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetModel.html\">UpdateAssetModel</a> operation. You can assign an external ID by specifying this value as part of a call to <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetModel.html\">UpdateAssetModel</a>. However, you can't change the external ID if one is already assigned. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids\">Using external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    name: "aws_sdk_iotsitewise.types.name.Name"
    """<p>The name of the asset model property.</p>"""
    data_type: "aws_sdk_iotsitewise.types.property_data_type.PropertyDataType"
    """<p>The data type of the asset model property.</p> <p>If you specify <code>STRUCT</code>, you must also specify <code>dataTypeSpec</code> to identify the type of the structure for this property.</p>"""
    data_type_spec: NotRequired["aws_sdk_iotsitewise.types.name.Name"]
    """<p>The data type of the structure for this property. This parameter exists on properties that have the <code>STRUCT</code> data type.</p>"""
    unit: NotRequired["aws_sdk_iotsitewise.types.property_unit.PropertyUnit"]
    """<p>The unit of the asset model property, such as <code>Newtons</code> or <code>RPM</code>.</p>"""
    type: "aws_sdk_iotsitewise.types.property_type.PropertyType"
    """<p>The property type (see <code>PropertyType</code>).</p>"""
    path: NotRequired[
        "aws_sdk_iotsitewise.types.asset_model_property_path.AssetModelPropertyPath"
    ]
    """<p>The structured path to the property from the root of the asset model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetModelProperty) -> dict:
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
    if "path" in value:
        import aws_sdk_iotsitewise.types.asset_model_property_path

        out["path"] = (
            aws_sdk_iotsitewise.types.asset_model_property_path.serialize_json(
                value["path"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssetModelProperty:
    out: AssetModelProperty = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "externalId" in data:
        out["external_id"] = data["externalId"]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AssetModelProperty.name required")
    if "dataType" in data:
        import aws_sdk_iotsitewise.types.property_data_type

        out["data_type"] = (
            aws_sdk_iotsitewise.types.property_data_type.deserialize_json(
                data["dataType"]
            )
        )
    else:
        raise DeserializationError("AssetModelProperty.data_type required")
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
        raise DeserializationError("AssetModelProperty.type required")
    if "path" in data:
        import aws_sdk_iotsitewise.types.asset_model_property_path

        out["path"] = (
            aws_sdk_iotsitewise.types.asset_model_property_path.deserialize_json(
                data["path"]
            )
        )
    return out
