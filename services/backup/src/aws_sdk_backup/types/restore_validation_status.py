"""Generated from Smithy shape ``com.amazonaws.backup#RestoreValidationStatus``."""

from typing import Literal, TypeAlias, cast

RestoreValidationStatus: TypeAlias = Literal[
    "FAILED",
    "SUCCESSFUL",
    "TIMED_OUT",
    "VALIDATING",
]


# --- restJson1 ser/de ---
def serialize_json(value: RestoreValidationStatus) -> str:
    return value


def deserialize_json(data: str) -> RestoreValidationStatus:
    return cast(RestoreValidationStatus, data)
