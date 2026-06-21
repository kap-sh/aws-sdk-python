"""Generated from Smithy shape ``com.amazonaws.quicksight#SectionPageBreakStatus``."""

from typing import Literal, TypeAlias, cast

SectionPageBreakStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: SectionPageBreakStatus) -> str:
    return value


def deserialize_json(data: str) -> SectionPageBreakStatus:
    return cast(SectionPageBreakStatus, data)
