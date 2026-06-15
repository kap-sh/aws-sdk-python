"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetProperty``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.asset_property_path
    import aws_sdk_iotsitewise.types.external_id
    import aws_sdk_iotsitewise.types.id
    import aws_sdk_iotsitewise.types.name
    import aws_sdk_iotsitewise.types.property_alias
    import aws_sdk_iotsitewise.types.property_data_type
    import aws_sdk_iotsitewise.types.property_notification
    import aws_sdk_iotsitewise.types.property_unit


class AssetProperty(TypedDict):
    id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the asset property.</p>"""
    external_id: NotRequired["aws_sdk_iotsitewise.types.external_id.ExternalId"]
    r"""<p>The external ID of the asset property. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids\">Using external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    name: "aws_sdk_iotsitewise.types.name.Name"
    """<p>The name of the property.</p>"""
    alias: NotRequired["aws_sdk_iotsitewise.types.property_alias.PropertyAlias"]
    r"""<p>The alias that identifies the property, such as an OPC-UA server data stream path (for example, <code>/company/windfarm/3/turbine/7/temperature</code>). For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html\">Mapping industrial data streams to asset properties</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    notification: NotRequired[
        "aws_sdk_iotsitewise.types.property_notification.PropertyNotification"
    ]
    r"""<p>The asset property's notification topic and state. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetProperty.html\">UpdateAssetProperty</a>.</p>"""
    data_type: "aws_sdk_iotsitewise.types.property_data_type.PropertyDataType"
    """<p>The data type of the asset property.</p>"""
    data_type_spec: NotRequired["aws_sdk_iotsitewise.types.name.Name"]
    """<p>The data type of the structure for this property. This parameter exists on properties that have the <code>STRUCT</code> data type.</p>"""
    unit: NotRequired["aws_sdk_iotsitewise.types.property_unit.PropertyUnit"]
    """<p>The unit (such as <code>Newtons</code> or <code>RPM</code>) of the asset property.</p>"""
    path: NotRequired["aws_sdk_iotsitewise.types.asset_property_path.AssetPropertyPath"]
    """<p>The structured path to the property from the root of the asset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetProperty) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    out["name"] = value["name"]
    if "alias" in value:
        out["alias"] = value["alias"]
    if "notification" in value:
        import aws_sdk_iotsitewise.types.property_notification

        out["notification"] = (
            aws_sdk_iotsitewise.types.property_notification.serialize_json(
                value["notification"]
            )
        )
    import aws_sdk_iotsitewise.types.property_data_type

    out["dataType"] = aws_sdk_iotsitewise.types.property_data_type.serialize_json(
        value["data_type"]
    )
    if "data_type_spec" in value:
        out["dataTypeSpec"] = value["data_type_spec"]
    if "unit" in value:
        out["unit"] = value["unit"]
    if "path" in value:
        import aws_sdk_iotsitewise.types.asset_property_path

        out["path"] = aws_sdk_iotsitewise.types.asset_property_path.serialize_json(
            value["path"]
        )
    return out


def deserialize_json(data: dict) -> AssetProperty:
    out: AssetProperty = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("AssetProperty.id required")
    if "externalId" in data:
        out["external_id"] = data["externalId"]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AssetProperty.name required")
    if "alias" in data:
        out["alias"] = data["alias"]
    if "notification" in data:
        import aws_sdk_iotsitewise.types.property_notification

        out["notification"] = (
            aws_sdk_iotsitewise.types.property_notification.deserialize_json(
                data["notification"]
            )
        )
    if "dataType" in data:
        import aws_sdk_iotsitewise.types.property_data_type

        out["data_type"] = (
            aws_sdk_iotsitewise.types.property_data_type.deserialize_json(
                data["dataType"]
            )
        )
    else:
        raise DeserializationError("AssetProperty.data_type required")
    if "dataTypeSpec" in data:
        out["data_type_spec"] = data["dataTypeSpec"]
    if "unit" in data:
        out["unit"] = data["unit"]
    if "path" in data:
        import aws_sdk_iotsitewise.types.asset_property_path

        out["path"] = aws_sdk_iotsitewise.types.asset_property_path.deserialize_json(
            data["path"]
        )
    return out
