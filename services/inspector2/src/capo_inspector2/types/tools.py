"""Generated from Smithy shape ``com.amazonaws.inspector2#Tools``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.tool

Tools: TypeAlias = list["capo_inspector2.types.tool.Tool"]


# --- restJson1 ser/de ---
def serialize_json(value: Tools) -> list:
    return list(value)


def deserialize_json(data: list) -> Tools:
    return list(data)
