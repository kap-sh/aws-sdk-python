"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfCmafIngestCaptionLanguageMapping``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.cmaf_ingest_caption_language_mapping

__listOfCmafIngestCaptionLanguageMapping: TypeAlias = list[
    "capo_medialive.types.cmaf_ingest_caption_language_mapping.CmafIngestCaptionLanguageMapping"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfCmafIngestCaptionLanguageMapping) -> list:
    import capo_medialive.types.cmaf_ingest_caption_language_mapping

    out: list = []
    for item in value:
        out.append(
            capo_medialive.types.cmaf_ingest_caption_language_mapping.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __listOfCmafIngestCaptionLanguageMapping:
    import capo_medialive.types.cmaf_ingest_caption_language_mapping

    out: __listOfCmafIngestCaptionLanguageMapping = []
    for item in data:
        out.append(
            capo_medialive.types.cmaf_ingest_caption_language_mapping.deserialize_json(
                item
            )
        )
    return out
