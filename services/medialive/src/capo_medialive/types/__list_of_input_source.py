"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfInputSource``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.input_source

__listOfInputSource: TypeAlias = list["capo_medialive.types.input_source.InputSource"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfInputSource) -> list:
    import capo_medialive.types.input_source

    out: list = []
    for item in value:
        out.append(capo_medialive.types.input_source.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfInputSource:
    import capo_medialive.types.input_source

    out: __listOfInputSource = []
    for item in data:
        out.append(capo_medialive.types.input_source.deserialize_json(item))
    return out
