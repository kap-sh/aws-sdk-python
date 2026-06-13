"""Generated from Smithy shape ``com.amazonaws.ssmsap#ApplicationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm_sap.errors import DeserializationError

ApplicationStatus: TypeAlias = Literal[
    "ACTIVATED",
    "STARTING",
    "STOPPED",
    "STOPPING",
    "FAILED",
    "REGISTERING",
    "DELETING",
    "UNKNOWN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVATED",
        "STARTING",
        "STOPPED",
        "STOPPING",
        "FAILED",
        "REGISTERING",
        "DELETING",
        "UNKNOWN",
    )
)


def serialize_json(value: ApplicationStatus) -> str:
    return value


def deserialize_json(data: str) -> ApplicationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ApplicationStatus value: {data!r}")
    return cast(ApplicationStatus, data)
