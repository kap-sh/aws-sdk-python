"""Generated from Smithy shape ``com.amazonaws.opensearch#MaintenanceType``."""

from typing import Literal, TypeAlias, cast

MaintenanceType: TypeAlias = Literal[
    "REBOOT_NODE",
    "RESTART_SEARCH_PROCESS",
    "RESTART_DASHBOARD",
]


# --- restJson1 ser/de ---
def serialize_json(value: MaintenanceType) -> str:
    return value


def deserialize_json(data: str) -> MaintenanceType:
    return cast(MaintenanceType, data)
