"""Generated from Smithy shape ``com.amazonaws.iotevents#InputIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.iot_events_input_identifier
    import aws_sdk_iot_events.types.iot_site_wise_input_identifier


class InputIdentifier(TypedDict, closed=True):
    iot_events_input_identifier: NotRequired[
        "aws_sdk_iot_events.types.iot_events_input_identifier.IotEventsInputIdentifier"
    ]
    """<p> The identifier of the input routed to AWS IoT Events. </p>"""
    iot_site_wise_input_identifier: NotRequired[
        "aws_sdk_iot_events.types.iot_site_wise_input_identifier.IotSiteWiseInputIdentifier"
    ]
    """<p> The identifer of the input routed from AWS IoT SiteWise. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InputIdentifier) -> dict:
    out: dict = {}
    if "iot_events_input_identifier" in value:
        import aws_sdk_iot_events.types.iot_events_input_identifier

        out["iotEventsInputIdentifier"] = (
            aws_sdk_iot_events.types.iot_events_input_identifier.serialize_json(
                value["iot_events_input_identifier"]
            )
        )
    if "iot_site_wise_input_identifier" in value:
        import aws_sdk_iot_events.types.iot_site_wise_input_identifier

        out["iotSiteWiseInputIdentifier"] = (
            aws_sdk_iot_events.types.iot_site_wise_input_identifier.serialize_json(
                value["iot_site_wise_input_identifier"]
            )
        )
    return out


def deserialize_json(data: dict) -> InputIdentifier:
    out: InputIdentifier = {}  # type: ignore[typeddict-item]
    if "iotEventsInputIdentifier" in data:
        import aws_sdk_iot_events.types.iot_events_input_identifier

        out["iot_events_input_identifier"] = (
            aws_sdk_iot_events.types.iot_events_input_identifier.deserialize_json(
                data["iotEventsInputIdentifier"]
            )
        )
    if "iotSiteWiseInputIdentifier" in data:
        import aws_sdk_iot_events.types.iot_site_wise_input_identifier

        out["iot_site_wise_input_identifier"] = (
            aws_sdk_iot_events.types.iot_site_wise_input_identifier.deserialize_json(
                data["iotSiteWiseInputIdentifier"]
            )
        )
    return out
