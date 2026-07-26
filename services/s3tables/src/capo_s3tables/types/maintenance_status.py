"""Generated from Smithy shape ``com.amazonaws.s3tables#MaintenanceStatus``."""

from typing import Literal, TypeAlias, cast

MaintenanceStatus: TypeAlias = Literal[
    "enabled",
    "disabled",
]


# --- restJson1 ser/de ---
def serialize_json(value: MaintenanceStatus) -> str:
    return value


def deserialize_json(data: str) -> MaintenanceStatus:
    return cast(MaintenanceStatus, data)
