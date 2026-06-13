"""Generated from Smithy shape ``com.amazonaws.ssmsap#DatabaseStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm_sap.errors import DeserializationError

DatabaseStatus: TypeAlias = Literal[
    "RUNNING",
    "STARTING",
    "STOPPED",
    "WARNING",
    "UNKNOWN",
    "ERROR",
    "STOPPING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RUNNING",
        "STARTING",
        "STOPPED",
        "WARNING",
        "UNKNOWN",
        "ERROR",
        "STOPPING",
    )
)


def serialize_json(value: DatabaseStatus) -> str:
    return value


def deserialize_json(data: str) -> DatabaseStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DatabaseStatus value: {data!r}")
    return cast(DatabaseStatus, data)
