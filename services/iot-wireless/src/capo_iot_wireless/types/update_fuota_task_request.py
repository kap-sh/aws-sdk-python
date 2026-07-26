"""Generated from Smithy shape ``com.amazonaws.iotwireless#UpdateFuotaTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.description
    import capo_iot_wireless.types.file_descriptor
    import capo_iot_wireless.types.firmware_update_image
    import capo_iot_wireless.types.firmware_update_role
    import capo_iot_wireless.types.fragment_interval_ms
    import capo_iot_wireless.types.fragment_size_bytes
    import capo_iot_wireless.types.fuota_task_id
    import capo_iot_wireless.types.fuota_task_name
    import capo_iot_wireless.types.lo_ra_wan_fuota_task
    import capo_iot_wireless.types.redundancy_percent


class UpdateFuotaTaskRequest(TypedDict, closed=True):
    id: "capo_iot_wireless.types.fuota_task_id.FuotaTaskId"
    name: NotRequired["capo_iot_wireless.types.fuota_task_name.FuotaTaskName"]
    description: NotRequired["capo_iot_wireless.types.description.Description"]
    lo_ra_wan: NotRequired[
        "capo_iot_wireless.types.lo_ra_wan_fuota_task.LoRaWANFuotaTask"
    ]
    firmware_update_image: NotRequired[
        "capo_iot_wireless.types.firmware_update_image.FirmwareUpdateImage"
    ]
    firmware_update_role: NotRequired[
        "capo_iot_wireless.types.firmware_update_role.FirmwareUpdateRole"
    ]
    redundancy_percent: NotRequired[
        "capo_iot_wireless.types.redundancy_percent.RedundancyPercent"
    ]
    fragment_size_bytes: NotRequired[
        "capo_iot_wireless.types.fragment_size_bytes.FragmentSizeBytes"
    ]
    fragment_interval_ms: NotRequired[
        "capo_iot_wireless.types.fragment_interval_ms.FragmentIntervalMS"
    ]
    descriptor: NotRequired["capo_iot_wireless.types.file_descriptor.FileDescriptor"]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFuotaTaskRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "lo_ra_wan" in value:
        import capo_iot_wireless.types.lo_ra_wan_fuota_task

        out["LoRaWAN"] = capo_iot_wireless.types.lo_ra_wan_fuota_task.serialize_json(
            value["lo_ra_wan"]
        )
    if "firmware_update_image" in value:
        out["FirmwareUpdateImage"] = value["firmware_update_image"]
    if "firmware_update_role" in value:
        out["FirmwareUpdateRole"] = value["firmware_update_role"]
    if "redundancy_percent" in value:
        out["RedundancyPercent"] = value["redundancy_percent"]
    if "fragment_size_bytes" in value:
        out["FragmentSizeBytes"] = value["fragment_size_bytes"]
    if "fragment_interval_ms" in value:
        out["FragmentIntervalMS"] = value["fragment_interval_ms"]
    if "descriptor" in value:
        out["Descriptor"] = value["descriptor"]
    return out


def deserialize_json(data: dict) -> UpdateFuotaTaskRequest:
    out: UpdateFuotaTaskRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "LoRaWAN" in data:
        import capo_iot_wireless.types.lo_ra_wan_fuota_task

        out["lo_ra_wan"] = (
            capo_iot_wireless.types.lo_ra_wan_fuota_task.deserialize_json(
                data["LoRaWAN"]
            )
        )
    if "FirmwareUpdateImage" in data:
        out["firmware_update_image"] = data["FirmwareUpdateImage"]
    if "FirmwareUpdateRole" in data:
        out["firmware_update_role"] = data["FirmwareUpdateRole"]
    if "RedundancyPercent" in data:
        out["redundancy_percent"] = data["RedundancyPercent"]
    if "FragmentSizeBytes" in data:
        out["fragment_size_bytes"] = data["FragmentSizeBytes"]
    if "FragmentIntervalMS" in data:
        out["fragment_interval_ms"] = data["FragmentIntervalMS"]
    if "Descriptor" in data:
        out["descriptor"] = data["Descriptor"]
    return out
