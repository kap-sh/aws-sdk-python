"""Generated from Smithy shape ``com.amazonaws.iotwireless#TestWirelessDeviceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.wireless_device_id


class TestWirelessDeviceRequest(TypedDict, closed=True):
    id: "aws_sdk_iot_wireless.types.wireless_device_id.WirelessDeviceId"
    """<p>The ID of the wireless device to test.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestWirelessDeviceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> TestWirelessDeviceRequest:
    out: TestWirelessDeviceRequest = {}  # type: ignore[typeddict-item]
    return out
