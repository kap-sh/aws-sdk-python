"""Generated from Smithy shape ``com.amazonaws.connect#SlaAssignmentType``."""

from typing import Literal, TypeAlias, cast

SlaAssignmentType: TypeAlias = Literal["CASES",]


# --- restJson1 ser/de ---
def serialize_json(value: SlaAssignmentType) -> str:
    return value


def deserialize_json(data: str) -> SlaAssignmentType:
    return cast(SlaAssignmentType, data)
