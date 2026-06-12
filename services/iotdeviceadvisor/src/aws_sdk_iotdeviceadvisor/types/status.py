"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#Status``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotdeviceadvisor.errors import DeserializationError

Status: TypeAlias = Literal[
    "PASS",
    "FAIL",
    "CANCELED",
    "PENDING",
    "RUNNING",
    "STOPPING",
    "STOPPED",
    "PASS_WITH_WARNINGS",
    "ERROR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PASS",
        "FAIL",
        "CANCELED",
        "PENDING",
        "RUNNING",
        "STOPPING",
        "STOPPED",
        "PASS_WITH_WARNINGS",
        "ERROR",
    )
)


def serialize_json(value: Status) -> str:
    return value


def deserialize_json(data: str) -> Status:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Status value: {data!r}")
    return cast(Status, data)
