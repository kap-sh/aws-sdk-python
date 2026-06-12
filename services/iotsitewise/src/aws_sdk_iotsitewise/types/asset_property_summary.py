"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetPropertySummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.asset_property_path
    import aws_sdk_iotsitewise.types.external_id
    import aws_sdk_iotsitewise.types.id
    import aws_sdk_iotsitewise.types.property_alias
    import aws_sdk_iotsitewise.types.property_notification
    import aws_sdk_iotsitewise.types.property_unit


class AssetPropertySummary(TypedDict):
    id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the property.</p>"""
    external_id: NotRequired["aws_sdk_iotsitewise.types.external_id.ExternalId"]
    """<p>The external ID of the property. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids\">Using external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    alias: NotRequired["aws_sdk_iotsitewise.types.property_alias.PropertyAlias"]
    """<p>The alias that identifies the property, such as an OPC-UA server data stream path (for example, <code>/company/windfarm/3/turbine/7/temperature</code>). For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html\">Mapping industrial data streams to asset properties</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    unit: NotRequired["aws_sdk_iotsitewise.types.property_unit.PropertyUnit"]
    """<p> The unit of measure (such as Newtons or RPM) of the asset property. </p>"""
    notification: NotRequired[
        "aws_sdk_iotsitewise.types.property_notification.PropertyNotification"
    ]
    asset_composite_model_id: NotRequired["aws_sdk_iotsitewise.types.id.ID"]
    """<p> The ID of the composite model that contains the asset property. </p>"""
    path: NotRequired["aws_sdk_iotsitewise.types.asset_property_path.AssetPropertyPath"]
    """<p>The structured path to the property from the root of the asset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetPropertySummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    if "alias" in value:
        out["alias"] = value["alias"]
    if "unit" in value:
        out["unit"] = value["unit"]
    if "notification" in value:
        import aws_sdk_iotsitewise.types.property_notification

        out["notification"] = (
            aws_sdk_iotsitewise.types.property_notification.serialize_json(
                value["notification"]
            )
        )
    if "asset_composite_model_id" in value:
        out["assetCompositeModelId"] = value["asset_composite_model_id"]
    if "path" in value:
        import aws_sdk_iotsitewise.types.asset_property_path

        out["path"] = aws_sdk_iotsitewise.types.asset_property_path.serialize_json(
            value["path"]
        )
    return out


def deserialize_json(data: dict) -> AssetPropertySummary:
    out: AssetPropertySummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("AssetPropertySummary.id required")
    if "externalId" in data:
        out["external_id"] = data["externalId"]
    if "alias" in data:
        out["alias"] = data["alias"]
    if "unit" in data:
        out["unit"] = data["unit"]
    if "notification" in data:
        import aws_sdk_iotsitewise.types.property_notification

        out["notification"] = (
            aws_sdk_iotsitewise.types.property_notification.deserialize_json(
                data["notification"]
            )
        )
    if "assetCompositeModelId" in data:
        out["asset_composite_model_id"] = data["assetCompositeModelId"]
    if "path" in data:
        import aws_sdk_iotsitewise.types.asset_property_path

        out["path"] = aws_sdk_iotsitewise.types.asset_property_path.deserialize_json(
            data["path"]
        )
    return out
