"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfOutputDestination``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.output_destination

__listOfOutputDestination: TypeAlias = list[
    "aws_sdk_medialive.types.output_destination.OutputDestination"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfOutputDestination) -> list:
    import aws_sdk_medialive.types.output_destination

    out: list = []
    for item in value:
        out.append(aws_sdk_medialive.types.output_destination.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfOutputDestination:
    import aws_sdk_medialive.types.output_destination

    out: __listOfOutputDestination = []
    for item in data:
        out.append(aws_sdk_medialive.types.output_destination.deserialize_json(item))
    return out
