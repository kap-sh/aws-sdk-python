"""Generated from Smithy shape ``com.amazonaws.iot#MaintenanceWindows``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.maintenance_window

MaintenanceWindows: TypeAlias = list[
    "aws_sdk_iot.types.maintenance_window.MaintenanceWindow"
]


# --- restJson1 ser/de ---
def serialize_json(value: MaintenanceWindows) -> list:
    import aws_sdk_iot.types.maintenance_window

    out: list = []
    for item in value:
        out.append(aws_sdk_iot.types.maintenance_window.serialize_json(item))
    return out


def deserialize_json(data: list) -> MaintenanceWindows:
    import aws_sdk_iot.types.maintenance_window

    out: MaintenanceWindows = []
    for item in data:
        out.append(aws_sdk_iot.types.maintenance_window.deserialize_json(item))
    return out
