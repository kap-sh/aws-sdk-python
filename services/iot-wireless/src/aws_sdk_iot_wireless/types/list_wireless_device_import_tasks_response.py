"""Generated from Smithy shape ``com.amazonaws.iotwireless#ListWirelessDeviceImportTasksResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.next_token
    import aws_sdk_iot_wireless.types.wireless_device_import_task_list


class ListWirelessDeviceImportTasksResponse(TypedDict):
    next_token: NotRequired["aws_sdk_iot_wireless.types.next_token.NextToken"]
    """<p>The token to use to get the next set of results, or <code>null</code> if there are no additional results.</p>"""
    wireless_device_import_task_list: NotRequired[
        "aws_sdk_iot_wireless.types.wireless_device_import_task_list.WirelessDeviceImportTaskList"
    ]
    """<p>List of import tasks and summary information of onboarding status of devices in each import task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWirelessDeviceImportTasksResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "wireless_device_import_task_list" in value:
        import aws_sdk_iot_wireless.types.wireless_device_import_task_list

        out["WirelessDeviceImportTaskList"] = (
            aws_sdk_iot_wireless.types.wireless_device_import_task_list.serialize_json(
                value["wireless_device_import_task_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListWirelessDeviceImportTasksResponse:
    out: ListWirelessDeviceImportTasksResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "WirelessDeviceImportTaskList" in data:
        import aws_sdk_iot_wireless.types.wireless_device_import_task_list

        out["wireless_device_import_task_list"] = (
            aws_sdk_iot_wireless.types.wireless_device_import_task_list.deserialize_json(
                data["WirelessDeviceImportTaskList"]
            )
        )
    return out
