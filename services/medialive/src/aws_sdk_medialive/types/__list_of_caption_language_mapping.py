"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfCaptionLanguageMapping``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.caption_language_mapping

__listOfCaptionLanguageMapping: TypeAlias = list[
    "aws_sdk_medialive.types.caption_language_mapping.CaptionLanguageMapping"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfCaptionLanguageMapping) -> list:
    import aws_sdk_medialive.types.caption_language_mapping

    out: list = []
    for item in value:
        out.append(
            aws_sdk_medialive.types.caption_language_mapping.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfCaptionLanguageMapping:
    import aws_sdk_medialive.types.caption_language_mapping

    out: __listOfCaptionLanguageMapping = []
    for item in data:
        out.append(
            aws_sdk_medialive.types.caption_language_mapping.deserialize_json(item)
        )
    return out
