"""Generated from Smithy shape ``com.amazonaws.ram#ResourceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ram.errors import DeserializationError

ResourceStatus: TypeAlias = Literal[
    "AVAILABLE",
    "ZONAL_RESOURCE_INACCESSIBLE",
    "LIMIT_EXCEEDED",
    "UNAVAILABLE",
    "PENDING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVAILABLE",
        "ZONAL_RESOURCE_INACCESSIBLE",
        "LIMIT_EXCEEDED",
        "UNAVAILABLE",
        "PENDING",
    )
)


def serialize_json(value: ResourceStatus) -> str:
    return value


def deserialize_json(data: str) -> ResourceStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceStatus value: {data!r}")
    return cast(ResourceStatus, data)
