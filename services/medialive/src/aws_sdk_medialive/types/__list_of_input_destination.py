"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfInputDestination``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.input_destination

__listOfInputDestination: TypeAlias = list[
    "aws_sdk_medialive.types.input_destination.InputDestination"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfInputDestination) -> list:
    import aws_sdk_medialive.types.input_destination

    out: list = []
    for item in value:
        out.append(aws_sdk_medialive.types.input_destination.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfInputDestination:
    import aws_sdk_medialive.types.input_destination

    out: __listOfInputDestination = []
    for item in data:
        out.append(aws_sdk_medialive.types.input_destination.deserialize_json(item))
    return out
