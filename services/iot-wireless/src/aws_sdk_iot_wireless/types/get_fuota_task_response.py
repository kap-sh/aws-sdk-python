"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetFuotaTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.created_at
    import aws_sdk_iot_wireless.types.description
    import aws_sdk_iot_wireless.types.file_descriptor
    import aws_sdk_iot_wireless.types.firmware_update_image
    import aws_sdk_iot_wireless.types.firmware_update_role
    import aws_sdk_iot_wireless.types.fragment_interval_ms
    import aws_sdk_iot_wireless.types.fragment_size_bytes
    import aws_sdk_iot_wireless.types.fuota_task_arn
    import aws_sdk_iot_wireless.types.fuota_task_id
    import aws_sdk_iot_wireless.types.fuota_task_name
    import aws_sdk_iot_wireless.types.fuota_task_status
    import aws_sdk_iot_wireless.types.lo_ra_wan_fuota_task_get_info
    import aws_sdk_iot_wireless.types.redundancy_percent


class GetFuotaTaskResponse(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_iot_wireless.types.fuota_task_arn.FuotaTaskArn"]
    id: NotRequired["aws_sdk_iot_wireless.types.fuota_task_id.FuotaTaskId"]
    status: NotRequired["aws_sdk_iot_wireless.types.fuota_task_status.FuotaTaskStatus"]
    name: NotRequired["aws_sdk_iot_wireless.types.fuota_task_name.FuotaTaskName"]
    description: NotRequired["aws_sdk_iot_wireless.types.description.Description"]
    lo_ra_wan: NotRequired[
        "aws_sdk_iot_wireless.types.lo_ra_wan_fuota_task_get_info.LoRaWANFuotaTaskGetInfo"
    ]
    firmware_update_image: NotRequired[
        "aws_sdk_iot_wireless.types.firmware_update_image.FirmwareUpdateImage"
    ]
    firmware_update_role: NotRequired[
        "aws_sdk_iot_wireless.types.firmware_update_role.FirmwareUpdateRole"
    ]
    created_at: NotRequired["aws_sdk_iot_wireless.types.created_at.CreatedAt"]
    redundancy_percent: NotRequired[
        "aws_sdk_iot_wireless.types.redundancy_percent.RedundancyPercent"
    ]
    fragment_size_bytes: NotRequired[
        "aws_sdk_iot_wireless.types.fragment_size_bytes.FragmentSizeBytes"
    ]
    fragment_interval_ms: NotRequired[
        "aws_sdk_iot_wireless.types.fragment_interval_ms.FragmentIntervalMS"
    ]
    descriptor: NotRequired["aws_sdk_iot_wireless.types.file_descriptor.FileDescriptor"]


# --- restJson1 ser/de ---
def serialize_json(value: GetFuotaTaskResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "id" in value:
        out["Id"] = value["id"]
    if "status" in value:
        import aws_sdk_iot_wireless.types.fuota_task_status

        out["Status"] = aws_sdk_iot_wireless.types.fuota_task_status.serialize_json(
            value["status"]
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "lo_ra_wan" in value:
        import aws_sdk_iot_wireless.types.lo_ra_wan_fuota_task_get_info

        out["LoRaWAN"] = (
            aws_sdk_iot_wireless.types.lo_ra_wan_fuota_task_get_info.serialize_json(
                value["lo_ra_wan"]
            )
        )
    if "firmware_update_image" in value:
        out["FirmwareUpdateImage"] = value["firmware_update_image"]
    if "firmware_update_role" in value:
        out["FirmwareUpdateRole"] = value["firmware_update_role"]
    if "created_at" in value:
        import aws_sdk_iot_wireless.types.created_at

        out["CreatedAt"] = aws_sdk_iot_wireless.types.created_at.serialize_json(
            value["created_at"]
        )
    if "redundancy_percent" in value:
        out["RedundancyPercent"] = value["redundancy_percent"]
    if "fragment_size_bytes" in value:
        out["FragmentSizeBytes"] = value["fragment_size_bytes"]
    if "fragment_interval_ms" in value:
        out["FragmentIntervalMS"] = value["fragment_interval_ms"]
    if "descriptor" in value:
        out["Descriptor"] = value["descriptor"]
    return out


def deserialize_json(data: dict) -> GetFuotaTaskResponse:
    out: GetFuotaTaskResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Status" in data:
        import aws_sdk_iot_wireless.types.fuota_task_status

        out["status"] = aws_sdk_iot_wireless.types.fuota_task_status.deserialize_json(
            data["Status"]
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "LoRaWAN" in data:
        import aws_sdk_iot_wireless.types.lo_ra_wan_fuota_task_get_info

        out["lo_ra_wan"] = (
            aws_sdk_iot_wireless.types.lo_ra_wan_fuota_task_get_info.deserialize_json(
                data["LoRaWAN"]
            )
        )
    if "FirmwareUpdateImage" in data:
        out["firmware_update_image"] = data["FirmwareUpdateImage"]
    if "FirmwareUpdateRole" in data:
        out["firmware_update_role"] = data["FirmwareUpdateRole"]
    if "CreatedAt" in data:
        import aws_sdk_iot_wireless.types.created_at

        out["created_at"] = aws_sdk_iot_wireless.types.created_at.deserialize_json(
            data["CreatedAt"]
        )
    if "RedundancyPercent" in data:
        out["redundancy_percent"] = data["RedundancyPercent"]
    if "FragmentSizeBytes" in data:
        out["fragment_size_bytes"] = data["FragmentSizeBytes"]
    if "FragmentIntervalMS" in data:
        out["fragment_interval_ms"] = data["FragmentIntervalMS"]
    if "Descriptor" in data:
        out["descriptor"] = data["Descriptor"]
    return out
