"""Generated from Smithy shape ``com.amazonaws.iotwireless#WirelessDeviceImportTask``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.creation_time
    import capo_iot_wireless.types.destination_name
    import capo_iot_wireless.types.import_task_arn
    import capo_iot_wireless.types.import_task_id
    import capo_iot_wireless.types.import_task_status
    import capo_iot_wireless.types.imported_wireless_device_count
    import capo_iot_wireless.types.positioning_config_status
    import capo_iot_wireless.types.sidewalk_get_start_import_info
    import capo_iot_wireless.types.status_reason


class WirelessDeviceImportTask(TypedDict, closed=True):
    id: NotRequired["capo_iot_wireless.types.import_task_id.ImportTaskId"]
    """<p>The ID of the wireless device import task.</p>"""
    arn: NotRequired["capo_iot_wireless.types.import_task_arn.ImportTaskArn"]
    """<p>The ARN (Amazon Resource Name) of the wireless device import task.</p>"""
    destination_name: NotRequired[
        "capo_iot_wireless.types.destination_name.DestinationName"
    ]
    """<p>The name of the Sidewalk destination that that describes the IoT rule to route messages from the device in the import task that will be onboarded to AWS IoT Wireless</p>"""
    positioning: NotRequired[
        "capo_iot_wireless.types.positioning_config_status.PositioningConfigStatus"
    ]
    """<p>The integration status of the Device Location feature for Sidewalk devices.</p>"""
    sidewalk: NotRequired[
        "capo_iot_wireless.types.sidewalk_get_start_import_info.SidewalkGetStartImportInfo"
    ]
    """<p>The Sidewalk-related information of the wireless device import task.</p>"""
    creation_time: NotRequired["capo_iot_wireless.types.creation_time.CreationTime"]
    """<p>The time at which the import task was created.</p>"""
    status: NotRequired["capo_iot_wireless.types.import_task_status.ImportTaskStatus"]
    """<p>The status information of the wireless device import task.</p>"""
    status_reason: NotRequired["capo_iot_wireless.types.status_reason.StatusReason"]
    """<p>The reason that provides additional information about the import task status.</p>"""
    initialized_imported_device_count: NotRequired[
        "capo_iot_wireless.types.imported_wireless_device_count.ImportedWirelessDeviceCount"
    ]
    """<p>The summary information of count of wireless devices that are waiting for the control log to be added to an import task.</p>"""
    pending_imported_device_count: NotRequired[
        "capo_iot_wireless.types.imported_wireless_device_count.ImportedWirelessDeviceCount"
    ]
    """<p>The summary information of count of wireless devices in an import task that are waiting in the queue to be onboarded.</p>"""
    onboarded_imported_device_count: NotRequired[
        "capo_iot_wireless.types.imported_wireless_device_count.ImportedWirelessDeviceCount"
    ]
    """<p>The summary information of count of wireless devices in an import task that have been onboarded to the import task.</p>"""
    failed_imported_device_count: NotRequired[
        "capo_iot_wireless.types.imported_wireless_device_count.ImportedWirelessDeviceCount"
    ]
    """<p>The summary information of count of wireless devices in an import task that failed to onboarded to the import task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WirelessDeviceImportTask) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
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
        import capo_iot_wireless.types.sidewalk_get_start_import_info

        out["Sidewalk"] = (
            capo_iot_wireless.types.sidewalk_get_start_import_info.serialize_json(
                value["sidewalk"]
            )
        )
    if "creation_time" in value:
        import capo_iot_wireless.types.creation_time

        out["CreationTime"] = capo_iot_wireless.types.creation_time.serialize_json(
            value["creation_time"]
        )
    if "status" in value:
        import capo_iot_wireless.types.import_task_status

        out["Status"] = capo_iot_wireless.types.import_task_status.serialize_json(
            value["status"]
        )
    if "status_reason" in value:
        out["StatusReason"] = value["status_reason"]
    if "initialized_imported_device_count" in value:
        out["InitializedImportedDeviceCount"] = value[
            "initialized_imported_device_count"
        ]
    if "pending_imported_device_count" in value:
        out["PendingImportedDeviceCount"] = value["pending_imported_device_count"]
    if "onboarded_imported_device_count" in value:
        out["OnboardedImportedDeviceCount"] = value["onboarded_imported_device_count"]
    if "failed_imported_device_count" in value:
        out["FailedImportedDeviceCount"] = value["failed_imported_device_count"]
    return out


def deserialize_json(data: dict) -> WirelessDeviceImportTask:
    out: WirelessDeviceImportTask = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
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
        import capo_iot_wireless.types.sidewalk_get_start_import_info

        out["sidewalk"] = (
            capo_iot_wireless.types.sidewalk_get_start_import_info.deserialize_json(
                data["Sidewalk"]
            )
        )
    if "CreationTime" in data:
        import capo_iot_wireless.types.creation_time

        out["creation_time"] = capo_iot_wireless.types.creation_time.deserialize_json(
            data["CreationTime"]
        )
    if "Status" in data:
        import capo_iot_wireless.types.import_task_status

        out["status"] = capo_iot_wireless.types.import_task_status.deserialize_json(
            data["Status"]
        )
    if "StatusReason" in data:
        out["status_reason"] = data["StatusReason"]
    if "InitializedImportedDeviceCount" in data:
        out["initialized_imported_device_count"] = data[
            "InitializedImportedDeviceCount"
        ]
    if "PendingImportedDeviceCount" in data:
        out["pending_imported_device_count"] = data["PendingImportedDeviceCount"]
    if "OnboardedImportedDeviceCount" in data:
        out["onboarded_imported_device_count"] = data["OnboardedImportedDeviceCount"]
    if "FailedImportedDeviceCount" in data:
        out["failed_imported_device_count"] = data["FailedImportedDeviceCount"]
    return out
