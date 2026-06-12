"""Generated from Smithy shape ``com.amazonaws.iotwireless#ListDevicesForWirelessDeviceImportTaskRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.import_task_id
    import aws_sdk_iot_wireless.types.max_results
    import aws_sdk_iot_wireless.types.next_token
    import aws_sdk_iot_wireless.types.onboard_status


class ListDevicesForWirelessDeviceImportTaskRequest(TypedDict):
    id: "aws_sdk_iot_wireless.types.import_task_id.ImportTaskId"
    """<p>The identifier of the import task for which wireless devices are listed.</p>"""
    max_results: "aws_sdk_iot_wireless.types.max_results.MaxResults"
    next_token: NotRequired["aws_sdk_iot_wireless.types.next_token.NextToken"]
    """<p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <code>null</code> to receive the first set of results.</p>"""
    status: NotRequired["aws_sdk_iot_wireless.types.onboard_status.OnboardStatus"]
    """<p>The status of the devices in the import task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDevicesForWirelessDeviceImportTaskRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDevicesForWirelessDeviceImportTaskRequest:
    out: ListDevicesForWirelessDeviceImportTaskRequest = {}  # type: ignore[typeddict-item]
    return out
