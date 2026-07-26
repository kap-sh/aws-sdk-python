"""Generated from Smithy shape ``com.amazonaws.braket#String256List``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_braket.types.string256

String256List: TypeAlias = list["capo_braket.types.string256.String256"]


# --- restJson1 ser/de ---
def serialize_json(value: String256List) -> list:
    return list(value)


def deserialize_json(data: list) -> String256List:
    return list(data)
