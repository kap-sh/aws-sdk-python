"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfInputSourceRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.input_source_request

__listOfInputSourceRequest: TypeAlias = list[
    "aws_sdk_medialive.types.input_source_request.InputSourceRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfInputSourceRequest) -> list:
    import aws_sdk_medialive.types.input_source_request

    out: list = []
    for item in value:
        out.append(aws_sdk_medialive.types.input_source_request.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfInputSourceRequest:
    import aws_sdk_medialive.types.input_source_request

    out: __listOfInputSourceRequest = []
    for item in data:
        out.append(aws_sdk_medialive.types.input_source_request.deserialize_json(item))
    return out
