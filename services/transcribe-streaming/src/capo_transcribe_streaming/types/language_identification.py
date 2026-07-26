"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#LanguageIdentification``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transcribe_streaming.types.language_with_score

LanguageIdentification: TypeAlias = list[
    "capo_transcribe_streaming.types.language_with_score.LanguageWithScore"
]


# --- restJson1 ser/de ---
def serialize_json(value: LanguageIdentification) -> list:
    import capo_transcribe_streaming.types.language_with_score

    out: list = []
    for item in value:
        out.append(
            capo_transcribe_streaming.types.language_with_score.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> LanguageIdentification:
    import capo_transcribe_streaming.types.language_with_score

    out: LanguageIdentification = []
    for item in data:
        out.append(
            capo_transcribe_streaming.types.language_with_score.deserialize_json(item)
        )
    return out
