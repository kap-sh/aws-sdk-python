"""Generated from Smithy shape ``com.amazonaws.iotwireless#TestWirelessDeviceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.result


class TestWirelessDeviceResponse(TypedDict, closed=True):
    result: NotRequired["capo_iot_wireless.types.result.Result"]
    """<p>The result returned by the test.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestWirelessDeviceResponse) -> dict:
    out: dict = {}
    if "result" in value:
        out["Result"] = value["result"]
    return out


def deserialize_json(data: dict) -> TestWirelessDeviceResponse:
    out: TestWirelessDeviceResponse = {}  # type: ignore[typeddict-item]
    if "Result" in data:
        out["result"] = data["Result"]
    return out
