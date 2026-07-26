"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfInputSourceRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.input_source_request

__listOfInputSourceRequest: TypeAlias = list[
    "capo_medialive.types.input_source_request.InputSourceRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfInputSourceRequest) -> list:
    import capo_medialive.types.input_source_request

    out: list = []
    for item in value:
        out.append(capo_medialive.types.input_source_request.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfInputSourceRequest:
    import capo_medialive.types.input_source_request

    out: __listOfInputSourceRequest = []
    for item in data:
        out.append(capo_medialive.types.input_source_request.deserialize_json(item))
    return out
