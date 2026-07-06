"""Generated from Smithy shape ``com.amazonaws.mediaconnect#MaintenanceSchedule``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_mediaconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.window_maintenance_schedule


class _MaintenanceSchedule_Window(TypedDict, closed=True):
    Window: "aws_sdk_mediaconnect.types.window_maintenance_schedule.WindowMaintenanceSchedule"


MaintenanceSchedule: TypeAlias = _MaintenanceSchedule_Window


# --- restJson1 ser/de ---
def serialize_json(value: MaintenanceSchedule) -> dict:
    if "Window" in value:
        import aws_sdk_mediaconnect.types.window_maintenance_schedule

        return {
            "window": aws_sdk_mediaconnect.types.window_maintenance_schedule.serialize_json(
                value["Window"]
            )
        }
    else:
        raise SerializationError("MaintenanceSchedule: no variant present")


def deserialize_json(data: dict) -> MaintenanceSchedule:
    if "window" in data:
        import aws_sdk_mediaconnect.types.window_maintenance_schedule

        return {
            "Window": aws_sdk_mediaconnect.types.window_maintenance_schedule.deserialize_json(
                data["window"]
            )
        }
    else:
        raise DeserializationError("MaintenanceSchedule: no recognized variant key")
