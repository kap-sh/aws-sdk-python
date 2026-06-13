"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#Status``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm_quicksetup.errors import DeserializationError

Status: TypeAlias = Literal[
    "INITIALIZING",
    "DEPLOYING",
    "SUCCEEDED",
    "DELETING",
    "STOPPING",
    "FAILED",
    "STOPPED",
    "DELETE_FAILED",
    "STOP_FAILED",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INITIALIZING",
        "DEPLOYING",
        "SUCCEEDED",
        "DELETING",
        "STOPPING",
        "FAILED",
        "STOPPED",
        "DELETE_FAILED",
        "STOP_FAILED",
        "NONE",
    )
)


def serialize_json(value: Status) -> str:
    return value


def deserialize_json(data: str) -> Status:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Status value: {data!r}")
    return cast(Status, data)
