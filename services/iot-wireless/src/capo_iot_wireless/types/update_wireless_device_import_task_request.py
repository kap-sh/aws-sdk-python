"""Generated from Smithy shape ``com.amazonaws.iotwireless#UpdateWirelessDeviceImportTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iot_wireless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot_wireless.types.import_task_id
    import capo_iot_wireless.types.sidewalk_update_import_info


class UpdateWirelessDeviceImportTaskRequest(TypedDict, closed=True):
    id: "capo_iot_wireless.types.import_task_id.ImportTaskId"
    """<p>The identifier of the import task to be updated.</p>"""
    sidewalk: (
        "capo_iot_wireless.types.sidewalk_update_import_info.SidewalkUpdateImportInfo"
    )
    """<p>The Sidewalk-related parameters of the import task to be updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWirelessDeviceImportTaskRequest) -> dict:
    out: dict = {}
    import capo_iot_wireless.types.sidewalk_update_import_info

    out["Sidewalk"] = (
        capo_iot_wireless.types.sidewalk_update_import_info.serialize_json(
            value["sidewalk"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateWirelessDeviceImportTaskRequest:
    out: UpdateWirelessDeviceImportTaskRequest = {}  # type: ignore[typeddict-item]
    if "Sidewalk" in data:
        import capo_iot_wireless.types.sidewalk_update_import_info

        out["sidewalk"] = (
            capo_iot_wireless.types.sidewalk_update_import_info.deserialize_json(
                data["Sidewalk"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateWirelessDeviceImportTaskRequest.sidewalk required"
        )
    return out
