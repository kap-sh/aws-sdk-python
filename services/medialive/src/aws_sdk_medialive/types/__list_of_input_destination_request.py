"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfInputDestinationRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.input_destination_request

__listOfInputDestinationRequest: TypeAlias = list[
    "aws_sdk_medialive.types.input_destination_request.InputDestinationRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfInputDestinationRequest) -> list:
    import aws_sdk_medialive.types.input_destination_request

    out: list = []
    for item in value:
        out.append(
            aws_sdk_medialive.types.input_destination_request.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfInputDestinationRequest:
    import aws_sdk_medialive.types.input_destination_request

    out: __listOfInputDestinationRequest = []
    for item in data:
        out.append(
            aws_sdk_medialive.types.input_destination_request.deserialize_json(item)
        )
    return out
