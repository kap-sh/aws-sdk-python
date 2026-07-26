"""Generated from Smithy shape ``com.amazonaws.groundstation#ContactStatus``."""

from typing import Literal, TypeAlias, cast

ContactStatus: TypeAlias = Literal[
    "SCHEDULING",
    "FAILED_TO_SCHEDULE",
    "SCHEDULED",
    "CANCELLED",
    "AWS_CANCELLED",
    "PREPASS",
    "PASS",
    "POSTPASS",
    "COMPLETED",
    "FAILED",
    "AVAILABLE",
    "CANCELLING",
    "AWS_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ContactStatus) -> str:
    return value


def deserialize_json(data: str) -> ContactStatus:
    return cast(ContactStatus, data)
