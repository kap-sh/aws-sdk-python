"""Generated from Smithy shape ``com.amazonaws.inspector2#TagComparison``."""

from typing import Literal, TypeAlias, cast

TagComparison: TypeAlias = Literal["EQUALS",]


# --- restJson1 ser/de ---
def serialize_json(value: TagComparison) -> str:
    return value


def deserialize_json(data: str) -> TagComparison:
    return cast(TagComparison, data)
