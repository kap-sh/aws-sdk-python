"""Generated from Smithy shape ``com.amazonaws.groundstation#EphemerisInvalidReason``."""

from typing import Literal, TypeAlias, cast

EphemerisInvalidReason: TypeAlias = Literal[
    "METADATA_INVALID",
    "TIME_RANGE_INVALID",
    "TRAJECTORY_INVALID",
    "KMS_KEY_INVALID",
    "VALIDATION_ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: EphemerisInvalidReason) -> str:
    return value


def deserialize_json(data: str) -> EphemerisInvalidReason:
    return cast(EphemerisInvalidReason, data)
