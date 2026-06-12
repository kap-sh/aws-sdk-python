"""Generated from Smithy shape ``com.amazonaws.opensearch#MaintenanceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

MaintenanceType: TypeAlias = Literal[
    "REBOOT_NODE",
    "RESTART_SEARCH_PROCESS",
    "RESTART_DASHBOARD",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REBOOT_NODE",
        "RESTART_SEARCH_PROCESS",
        "RESTART_DASHBOARD",
    )
)


def serialize_json(value: MaintenanceType) -> str:
    return value


def deserialize_json(data: str) -> MaintenanceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MaintenanceType value: {data!r}")
    return cast(MaintenanceType, data)
