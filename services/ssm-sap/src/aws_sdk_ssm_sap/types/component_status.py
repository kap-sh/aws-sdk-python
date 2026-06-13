"""Generated from Smithy shape ``com.amazonaws.ssmsap#ComponentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm_sap.errors import DeserializationError

ComponentStatus: TypeAlias = Literal[
    "ACTIVATED",
    "STARTING",
    "STOPPED",
    "STOPPING",
    "RUNNING",
    "RUNNING_WITH_ERROR",
    "UNDEFINED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVATED",
        "STARTING",
        "STOPPED",
        "STOPPING",
        "RUNNING",
        "RUNNING_WITH_ERROR",
        "UNDEFINED",
    )
)


def serialize_json(value: ComponentStatus) -> str:
    return value


def deserialize_json(data: str) -> ComponentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ComponentStatus value: {data!r}")
    return cast(ComponentStatus, data)
