"""Generated from Smithy shape ``com.amazonaws.iotwireless#ListDevicesForWirelessDeviceImportTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.destination_name
    import capo_iot_wireless.types.imported_wireless_device_list
    import capo_iot_wireless.types.next_token
    import capo_iot_wireless.types.positioning_config_status
    import capo_iot_wireless.types.sidewalk_list_devices_for_import_info


class ListDevicesForWirelessDeviceImportTaskResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_iot_wireless.types.next_token.NextToken"]
    """<p>The token to use to get the next set of results, or <code>null</code> if there are no additional results.</p>"""
    destination_name: NotRequired[
        "capo_iot_wireless.types.destination_name.DestinationName"
    ]
    """<p>The name of the Sidewalk destination that describes the IoT rule to route messages received from devices in an import task that are onboarded to AWS IoT Wireless.</p>"""
    positioning: NotRequired[
        "capo_iot_wireless.types.positioning_config_status.PositioningConfigStatus"
    ]
    """<p>The integration status of the Device Location feature for Sidewalk devices.</p>"""
    sidewalk: NotRequired[
        "capo_iot_wireless.types.sidewalk_list_devices_for_import_info.SidewalkListDevicesForImportInfo"
    ]
    """<p>The Sidewalk object containing Sidewalk-related device information.</p>"""
    imported_wireless_device_list: NotRequired[
        "capo_iot_wireless.types.imported_wireless_device_list.ImportedWirelessDeviceList"
    ]
    """<p>List of wireless devices in an import task and their onboarding status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDevicesForWirelessDeviceImportTaskResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "destination_name" in value:
        out["DestinationName"] = value["destination_name"]
    if "positioning" in value:
        import capo_iot_wireless.types.positioning_config_status

        out["Positioning"] = (
            capo_iot_wireless.types.positioning_config_status.serialize_json(
                value["positioning"]
            )
        )
    if "sidewalk" in value:
        import capo_iot_wireless.types.sidewalk_list_devices_for_import_info

        out["Sidewalk"] = (
            capo_iot_wireless.types.sidewalk_list_devices_for_import_info.serialize_json(
                value["sidewalk"]
            )
        )
    if "imported_wireless_device_list" in value:
        import capo_iot_wireless.types.imported_wireless_device_list

        out["ImportedWirelessDeviceList"] = (
            capo_iot_wireless.types.imported_wireless_device_list.serialize_json(
                value["imported_wireless_device_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListDevicesForWirelessDeviceImportTaskResponse:
    out: ListDevicesForWirelessDeviceImportTaskResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "DestinationName" in data:
        out["destination_name"] = data["DestinationName"]
    if "Positioning" in data:
        import capo_iot_wireless.types.positioning_config_status

        out["positioning"] = (
            capo_iot_wireless.types.positioning_config_status.deserialize_json(
                data["Positioning"]
            )
        )
    if "Sidewalk" in data:
        import capo_iot_wireless.types.sidewalk_list_devices_for_import_info

        out["sidewalk"] = (
            capo_iot_wireless.types.sidewalk_list_devices_for_import_info.deserialize_json(
                data["Sidewalk"]
            )
        )
    if "ImportedWirelessDeviceList" in data:
        import capo_iot_wireless.types.imported_wireless_device_list

        out["imported_wireless_device_list"] = (
            capo_iot_wireless.types.imported_wireless_device_list.deserialize_json(
                data["ImportedWirelessDeviceList"]
            )
        )
    return out
