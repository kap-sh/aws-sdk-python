"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#SoftwareSetValidationStatus``."""

from typing import Literal, TypeAlias, cast

SoftwareSetValidationStatus: TypeAlias = Literal[
    "VALIDATED",
    "NOT_VALIDATED",
]


# --- restJson1 ser/de ---
def serialize_json(value: SoftwareSetValidationStatus) -> str:
    return value


def deserialize_json(data: str) -> SoftwareSetValidationStatus:
    return cast(SoftwareSetValidationStatus, data)
