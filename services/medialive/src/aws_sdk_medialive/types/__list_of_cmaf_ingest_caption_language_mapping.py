"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfCmafIngestCaptionLanguageMapping``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.cmaf_ingest_caption_language_mapping

__listOfCmafIngestCaptionLanguageMapping: TypeAlias = list[
    "aws_sdk_medialive.types.cmaf_ingest_caption_language_mapping.CmafIngestCaptionLanguageMapping"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfCmafIngestCaptionLanguageMapping) -> list:
    import aws_sdk_medialive.types.cmaf_ingest_caption_language_mapping

    out: list = []
    for item in value:
        out.append(
            aws_sdk_medialive.types.cmaf_ingest_caption_language_mapping.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __listOfCmafIngestCaptionLanguageMapping:
    import aws_sdk_medialive.types.cmaf_ingest_caption_language_mapping

    out: __listOfCmafIngestCaptionLanguageMapping = []
    for item in data:
        out.append(
            aws_sdk_medialive.types.cmaf_ingest_caption_language_mapping.deserialize_json(
                item
            )
        )
    return out
