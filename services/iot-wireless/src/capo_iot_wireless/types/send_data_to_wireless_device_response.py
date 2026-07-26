"""Generated from Smithy shape ``com.amazonaws.iotwireless#SendDataToWirelessDeviceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.message_id


class SendDataToWirelessDeviceResponse(TypedDict, closed=True):
    message_id: NotRequired["capo_iot_wireless.types.message_id.MessageId"]
    """<p>The ID of the message sent to the wireless device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendDataToWirelessDeviceResponse) -> dict:
    out: dict = {}
    if "message_id" in value:
        out["MessageId"] = value["message_id"]
    return out


def deserialize_json(data: dict) -> SendDataToWirelessDeviceResponse:
    out: SendDataToWirelessDeviceResponse = {}  # type: ignore[typeddict-item]
    if "MessageId" in data:
        out["message_id"] = data["MessageId"]
    return out
