"""Generated from Smithy shape ``com.amazonaws.connectcases#ValuesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connectcases.types.value

ValuesList: TypeAlias = list["capo_connectcases.types.value.Value"]


# --- restJson1 ser/de ---
def serialize_json(value: ValuesList) -> list:
    return list(value)


def deserialize_json(data: list) -> ValuesList:
    return list(data)
