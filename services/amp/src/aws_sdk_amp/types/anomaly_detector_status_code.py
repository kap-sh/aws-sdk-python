"""Generated from Smithy shape ``com.amazonaws.amp#AnomalyDetectorStatusCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_amp.errors import DeserializationError

AnomalyDetectorStatusCode: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "UPDATING",
    "DELETING",
    "CREATION_FAILED",
    "UPDATE_FAILED",
    "DELETION_FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "ACTIVE",
        "UPDATING",
        "DELETING",
        "CREATION_FAILED",
        "UPDATE_FAILED",
        "DELETION_FAILED",
    )
)


def serialize_json(value: AnomalyDetectorStatusCode) -> str:
    return value


def deserialize_json(data: str) -> AnomalyDetectorStatusCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AnomalyDetectorStatusCode value: {data!r}")
    return cast(AnomalyDetectorStatusCode, data)
