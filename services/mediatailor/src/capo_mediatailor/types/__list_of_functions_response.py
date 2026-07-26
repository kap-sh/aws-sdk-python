"""Generated from Smithy shape ``com.amazonaws.mediatailor#__listOfFunctionsResponse``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediatailor.types.function

__listOfFunctionsResponse: TypeAlias = list["capo_mediatailor.types.function.Function"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfFunctionsResponse) -> list:
    import capo_mediatailor.types.function

    out: list = []
    for item in value:
        out.append(capo_mediatailor.types.function.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfFunctionsResponse:
    import capo_mediatailor.types.function

    out: __listOfFunctionsResponse = []
    for item in data:
        out.append(capo_mediatailor.types.function.deserialize_json(item))
    return out
