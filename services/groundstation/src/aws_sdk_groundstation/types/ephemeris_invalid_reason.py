"""Generated from Smithy shape ``com.amazonaws.groundstation#EphemerisInvalidReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_groundstation.errors import DeserializationError

EphemerisInvalidReason: TypeAlias = Literal[
    "METADATA_INVALID",
    "TIME_RANGE_INVALID",
    "TRAJECTORY_INVALID",
    "KMS_KEY_INVALID",
    "VALIDATION_ERROR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "METADATA_INVALID",
        "TIME_RANGE_INVALID",
        "TRAJECTORY_INVALID",
        "KMS_KEY_INVALID",
        "VALIDATION_ERROR",
    )
)


def serialize_json(value: EphemerisInvalidReason) -> str:
    return value


def deserialize_json(data: str) -> EphemerisInvalidReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EphemerisInvalidReason value: {data!r}")
    return cast(EphemerisInvalidReason, data)
