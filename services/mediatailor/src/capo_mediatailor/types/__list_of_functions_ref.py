"""Generated from Smithy shape ``com.amazonaws.mediatailor#__listOfFunctionsRef``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediatailor.types.function_ref

__listOfFunctionsRef: TypeAlias = list[
    "capo_mediatailor.types.function_ref.FunctionRef"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfFunctionsRef) -> list:
    import capo_mediatailor.types.function_ref

    out: list = []
    for item in value:
        out.append(capo_mediatailor.types.function_ref.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfFunctionsRef:
    import capo_mediatailor.types.function_ref

    out: __listOfFunctionsRef = []
    for item in data:
        out.append(capo_mediatailor.types.function_ref.deserialize_json(item))
    return out
