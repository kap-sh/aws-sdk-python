"""Generated from Smithy shape ``com.amazonaws.iotevents#IotSiteWiseInputIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.iot_site_wise_asset_model_property_identifier


class IotSiteWiseInputIdentifier(TypedDict, closed=True):
    iot_site_wise_asset_model_property_identifier: NotRequired[
        "capo_iot_events.types.iot_site_wise_asset_model_property_identifier.IotSiteWiseAssetModelPropertyIdentifier"
    ]
    """<p> The identifier of the AWS IoT SiteWise asset model property. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IotSiteWiseInputIdentifier) -> dict:
    out: dict = {}
    if "iot_site_wise_asset_model_property_identifier" in value:
        import capo_iot_events.types.iot_site_wise_asset_model_property_identifier

        out["iotSiteWiseAssetModelPropertyIdentifier"] = (
            capo_iot_events.types.iot_site_wise_asset_model_property_identifier.serialize_json(
                value["iot_site_wise_asset_model_property_identifier"]
            )
        )
    return out


def deserialize_json(data: dict) -> IotSiteWiseInputIdentifier:
    out: IotSiteWiseInputIdentifier = {}  # type: ignore[typeddict-item]
    if "iotSiteWiseAssetModelPropertyIdentifier" in data:
        import capo_iot_events.types.iot_site_wise_asset_model_property_identifier

        out["iot_site_wise_asset_model_property_identifier"] = (
            capo_iot_events.types.iot_site_wise_asset_model_property_identifier.deserialize_json(
                data["iotSiteWiseAssetModelPropertyIdentifier"]
            )
        )
    return out
