"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetModelPropertyDefinition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.external_id
    import aws_sdk_iotsitewise.types.id
    import aws_sdk_iotsitewise.types.name
    import aws_sdk_iotsitewise.types.property_data_type
    import aws_sdk_iotsitewise.types.property_type
    import aws_sdk_iotsitewise.types.property_unit


class AssetModelPropertyDefinition(TypedDict):
    id: NotRequired["aws_sdk_iotsitewise.types.id.ID"]
    """<p>The ID to assign to the asset model property, if desired. IoT SiteWise automatically generates a unique ID for you, so this parameter is never required. However, if you prefer to supply your own ID instead, you can specify it here in UUID format. If you specify your own ID, it must be globally unique.</p>"""
    external_id: NotRequired["aws_sdk_iotsitewise.types.external_id.ExternalId"]
    r"""<p>An external ID to assign to the property definition. The external ID must be unique among property definitions within this asset model. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids\">Using external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    name: "aws_sdk_iotsitewise.types.name.Name"
    """<p>The name of the property definition.</p>"""
    data_type: "aws_sdk_iotsitewise.types.property_data_type.PropertyDataType"
    """<p>The data type of the property definition.</p> <p>If you specify <code>STRUCT</code>, you must also specify <code>dataTypeSpec</code> to identify the type of the structure for this property.</p>"""
    data_type_spec: NotRequired["aws_sdk_iotsitewise.types.name.Name"]
    """<p>The data type of the structure for this property. This parameter is required on properties that have the <code>STRUCT</code> data type.</p> <p>The options for this parameter depend on the type of the composite model in which you define this property. Use <code>AWS/ALARM_STATE</code> for alarm state in alarm composite models.</p>"""
    unit: NotRequired["aws_sdk_iotsitewise.types.property_unit.PropertyUnit"]
    """<p>The unit of the property definition, such as <code>Newtons</code> or <code>RPM</code>.</p>"""
    type: "aws_sdk_iotsitewise.types.property_type.PropertyType"
    """<p>The property definition type (see <code>PropertyType</code>). You can only specify one type in a property definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetModelPropertyDefinition) -> dict:
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
    return out


def deserialize_json(data: dict) -> AssetModelPropertyDefinition:
    out: AssetModelPropertyDefinition = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "externalId" in data:
        out["external_id"] = data["externalId"]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AssetModelPropertyDefinition.name required")
    if "dataType" in data:
        import aws_sdk_iotsitewise.types.property_data_type

        out["data_type"] = (
            aws_sdk_iotsitewise.types.property_data_type.deserialize_json(
                data["dataType"]
            )
        )
    else:
        raise DeserializationError("AssetModelPropertyDefinition.data_type required")
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
        raise DeserializationError("AssetModelPropertyDefinition.type required")
    return out
