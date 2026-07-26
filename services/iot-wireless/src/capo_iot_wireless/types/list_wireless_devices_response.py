"""Generated from Smithy shape ``com.amazonaws.iotwireless#ListWirelessDevicesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.next_token
    import capo_iot_wireless.types.wireless_device_statistics_list


class ListWirelessDevicesResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_iot_wireless.types.next_token.NextToken"]
    """<p>The token to use to get the next set of results, or <b>null</b> if there are no additional results.</p>"""
    wireless_device_list: NotRequired[
        "capo_iot_wireless.types.wireless_device_statistics_list.WirelessDeviceStatisticsList"
    ]
    """<p>The ID of the wireless device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWirelessDevicesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "wireless_device_list" in value:
        import capo_iot_wireless.types.wireless_device_statistics_list

        out["WirelessDeviceList"] = (
            capo_iot_wireless.types.wireless_device_statistics_list.serialize_json(
                value["wireless_device_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListWirelessDevicesResponse:
    out: ListWirelessDevicesResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "WirelessDeviceList" in data:
        import capo_iot_wireless.types.wireless_device_statistics_list

        out["wireless_device_list"] = (
            capo_iot_wireless.types.wireless_device_statistics_list.deserialize_json(
                data["WirelessDeviceList"]
            )
        )
    return out
