"""Generated from Smithy shape ``com.amazonaws.iotevents#IotSiteWiseAssetModelPropertyIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iot_events.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.asset_model_id
    import aws_sdk_iot_events.types.asset_property_id


class IotSiteWiseAssetModelPropertyIdentifier(TypedDict, closed=True):
    asset_model_id: "aws_sdk_iot_events.types.asset_model_id.AssetModelId"
    """<p> The ID of the AWS IoT SiteWise asset model. </p>"""
    property_id: "aws_sdk_iot_events.types.asset_property_id.AssetPropertyId"
    """<p> The ID of the AWS IoT SiteWise asset property. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IotSiteWiseAssetModelPropertyIdentifier) -> dict:
    out: dict = {}
    out["assetModelId"] = value["asset_model_id"]
    out["propertyId"] = value["property_id"]
    return out


def deserialize_json(data: dict) -> IotSiteWiseAssetModelPropertyIdentifier:
    out: IotSiteWiseAssetModelPropertyIdentifier = {}  # type: ignore[typeddict-item]
    if "assetModelId" in data:
        out["asset_model_id"] = data["assetModelId"]
    else:
        raise DeserializationError(
            "IotSiteWiseAssetModelPropertyIdentifier.asset_model_id required"
        )
    if "propertyId" in data:
        out["property_id"] = data["propertyId"]
    else:
        raise DeserializationError(
            "IotSiteWiseAssetModelPropertyIdentifier.property_id required"
        )
    return out
