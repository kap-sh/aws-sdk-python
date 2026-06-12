"""Generated from Smithy shape ``com.amazonaws.iotevents#IotSiteWiseAction``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.asset_id
    import aws_sdk_iot_events.types.asset_property_alias
    import aws_sdk_iot_events.types.asset_property_entry_id
    import aws_sdk_iot_events.types.asset_property_id
    import aws_sdk_iot_events.types.asset_property_value


class IotSiteWiseAction(TypedDict):
    entry_id: NotRequired[
        "aws_sdk_iot_events.types.asset_property_entry_id.AssetPropertyEntryId"
    ]
    """<p>A unique identifier for this entry. You can use the entry ID to track which data entry causes an error in case of failure. The default is a new unique identifier.</p>"""
    asset_id: NotRequired["aws_sdk_iot_events.types.asset_id.AssetId"]
    """<p>The ID of the asset that has the specified property.</p>"""
    property_id: NotRequired[
        "aws_sdk_iot_events.types.asset_property_id.AssetPropertyId"
    ]
    """<p>The ID of the asset property.</p>"""
    property_alias: NotRequired[
        "aws_sdk_iot_events.types.asset_property_alias.AssetPropertyAlias"
    ]
    """<p>The alias of the asset property.</p>"""
    property_value: NotRequired[
        "aws_sdk_iot_events.types.asset_property_value.AssetPropertyValue"
    ]
    """<p>The value to send to the asset property. This value contains timestamp, quality, and value (TQV) information. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IotSiteWiseAction) -> dict:
    out: dict = {}
    if "entry_id" in value:
        out["entryId"] = value["entry_id"]
    if "asset_id" in value:
        out["assetId"] = value["asset_id"]
    if "property_id" in value:
        out["propertyId"] = value["property_id"]
    if "property_alias" in value:
        out["propertyAlias"] = value["property_alias"]
    if "property_value" in value:
        import aws_sdk_iot_events.types.asset_property_value

        out["propertyValue"] = (
            aws_sdk_iot_events.types.asset_property_value.serialize_json(
                value["property_value"]
            )
        )
    return out


def deserialize_json(data: dict) -> IotSiteWiseAction:
    out: IotSiteWiseAction = {}  # type: ignore[typeddict-item]
    if "entryId" in data:
        out["entry_id"] = data["entryId"]
    if "assetId" in data:
        out["asset_id"] = data["assetId"]
    if "propertyId" in data:
        out["property_id"] = data["propertyId"]
    if "propertyAlias" in data:
        out["property_alias"] = data["propertyAlias"]
    if "propertyValue" in data:
        import aws_sdk_iot_events.types.asset_property_value

        out["property_value"] = (
            aws_sdk_iot_events.types.asset_property_value.deserialize_json(
                data["propertyValue"]
            )
        )
    return out
