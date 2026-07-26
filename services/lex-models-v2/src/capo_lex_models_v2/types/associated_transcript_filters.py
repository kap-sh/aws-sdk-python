"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AssociatedTranscriptFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.associated_transcript_filter

AssociatedTranscriptFilters: TypeAlias = list[
    "capo_lex_models_v2.types.associated_transcript_filter.AssociatedTranscriptFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedTranscriptFilters) -> list:
    import capo_lex_models_v2.types.associated_transcript_filter

    out: list = []
    for item in value:
        out.append(
            capo_lex_models_v2.types.associated_transcript_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AssociatedTranscriptFilters:
    import capo_lex_models_v2.types.associated_transcript_filter

    out: AssociatedTranscriptFilters = []
    for item in data:
        out.append(
            capo_lex_models_v2.types.associated_transcript_filter.deserialize_json(item)
        )
    return out
