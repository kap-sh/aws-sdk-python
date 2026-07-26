"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ScalarFunctionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.scalar_functions

ScalarFunctionsList: TypeAlias = list[
    "capo_cleanrooms.types.scalar_functions.ScalarFunctions"
]


# --- restJson1 ser/de ---
def serialize_json(value: ScalarFunctionsList) -> list:
    return list(value)


def deserialize_json(data: list) -> ScalarFunctionsList:
    return list(data)
