"""Generated from Smithy shape ``com.amazonaws.iotwireless#ListQueuedMessagesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.max_results
    import aws_sdk_iot_wireless.types.next_token
    import aws_sdk_iot_wireless.types.wireless_device_id
    import aws_sdk_iot_wireless.types.wireless_device_type


class ListQueuedMessagesRequest(TypedDict):
    id: "aws_sdk_iot_wireless.types.wireless_device_id.WirelessDeviceId"
    """<p>The ID of a given wireless device which the downlink message packets are being sent.</p>"""
    next_token: NotRequired["aws_sdk_iot_wireless.types.next_token.NextToken"]
    """<p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>"""
    max_results: "aws_sdk_iot_wireless.types.max_results.MaxResults"
    """<p>The maximum number of results to return in this operation.</p>"""
    wireless_device_type: NotRequired[
        "aws_sdk_iot_wireless.types.wireless_device_type.WirelessDeviceType"
    ]
    """<p>The wireless device type, whic can be either Sidewalk or LoRaWAN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListQueuedMessagesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListQueuedMessagesRequest:
    out: ListQueuedMessagesRequest = {}  # type: ignore[typeddict-item]
    return out
