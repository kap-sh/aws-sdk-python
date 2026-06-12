"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfSrtOutputDestinationSettings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.srt_output_destination_settings

__listOfSrtOutputDestinationSettings: TypeAlias = list[
    "aws_sdk_medialive.types.srt_output_destination_settings.SrtOutputDestinationSettings"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfSrtOutputDestinationSettings) -> list:
    import aws_sdk_medialive.types.srt_output_destination_settings

    out: list = []
    for item in value:
        out.append(
            aws_sdk_medialive.types.srt_output_destination_settings.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfSrtOutputDestinationSettings:
    import aws_sdk_medialive.types.srt_output_destination_settings

    out: __listOfSrtOutputDestinationSettings = []
    for item in data:
        out.append(
            aws_sdk_medialive.types.srt_output_destination_settings.deserialize_json(
                item
            )
        )
    return out
