"""Generated from Smithy shape ``com.amazonaws.iot#MaintenanceWindows``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.maintenance_window

MaintenanceWindows: TypeAlias = list[
    "capo_iot.types.maintenance_window.MaintenanceWindow"
]


# --- restJson1 ser/de ---
def serialize_json(value: MaintenanceWindows) -> list:
    import capo_iot.types.maintenance_window

    out: list = []
    for item in value:
        out.append(capo_iot.types.maintenance_window.serialize_json(item))
    return out


def deserialize_json(data: list) -> MaintenanceWindows:
    import capo_iot.types.maintenance_window

    out: MaintenanceWindows = []
    for item in data:
        out.append(capo_iot.types.maintenance_window.deserialize_json(item))
    return out
