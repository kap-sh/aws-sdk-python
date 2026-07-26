"""Generated from Smithy shape ``com.amazonaws.iotwireless#ListDeviceProfilesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.device_profile_list
    import capo_iot_wireless.types.next_token


class ListDeviceProfilesResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_iot_wireless.types.next_token.NextToken"]
    """<p>The token to use to get the next set of results, or <b>null</b> if there are no additional results.</p>"""
    device_profile_list: NotRequired[
        "capo_iot_wireless.types.device_profile_list.DeviceProfileList"
    ]
    """<p>The list of device profiles.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDeviceProfilesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "device_profile_list" in value:
        import capo_iot_wireless.types.device_profile_list

        out["DeviceProfileList"] = (
            capo_iot_wireless.types.device_profile_list.serialize_json(
                value["device_profile_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListDeviceProfilesResponse:
    out: ListDeviceProfilesResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "DeviceProfileList" in data:
        import capo_iot_wireless.types.device_profile_list

        out["device_profile_list"] = (
            capo_iot_wireless.types.device_profile_list.deserialize_json(
                data["DeviceProfileList"]
            )
        )
    return out
