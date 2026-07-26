"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfInput``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.input

__listOfInput: TypeAlias = list["capo_medialive.types.input.Input"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfInput) -> list:
    import capo_medialive.types.input

    out: list = []
    for item in value:
        out.append(capo_medialive.types.input.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfInput:
    import capo_medialive.types.input

    out: __listOfInput = []
    for item in data:
        out.append(capo_medialive.types.input.deserialize_json(item))
    return out
