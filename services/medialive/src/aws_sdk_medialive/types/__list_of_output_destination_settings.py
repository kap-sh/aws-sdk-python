"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfOutputDestinationSettings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.output_destination_settings

__listOfOutputDestinationSettings: TypeAlias = list[
    "aws_sdk_medialive.types.output_destination_settings.OutputDestinationSettings"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfOutputDestinationSettings) -> list:
    import aws_sdk_medialive.types.output_destination_settings

    out: list = []
    for item in value:
        out.append(
            aws_sdk_medialive.types.output_destination_settings.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfOutputDestinationSettings:
    import aws_sdk_medialive.types.output_destination_settings

    out: __listOfOutputDestinationSettings = []
    for item in data:
        out.append(
            aws_sdk_medialive.types.output_destination_settings.deserialize_json(item)
        )
    return out
