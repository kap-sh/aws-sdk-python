"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetDevicesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.device_list
    import aws_sdk_networkmanager.types.next_token


class GetDevicesResponse(TypedDict):
    devices: NotRequired["aws_sdk_networkmanager.types.device_list.DeviceList"]
    """<p>The devices.</p>"""
    next_token: NotRequired["aws_sdk_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDevicesResponse) -> dict:
    out: dict = {}
    if "devices" in value:
        import aws_sdk_networkmanager.types.device_list

        out["Devices"] = aws_sdk_networkmanager.types.device_list.serialize_json(
            value["devices"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetDevicesResponse:
    out: GetDevicesResponse = {}  # type: ignore[typeddict-item]
    if "Devices" in data:
        import aws_sdk_networkmanager.types.device_list

        out["devices"] = aws_sdk_networkmanager.types.device_list.deserialize_json(
            data["Devices"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
