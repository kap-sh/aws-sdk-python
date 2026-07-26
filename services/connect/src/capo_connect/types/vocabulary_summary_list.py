"""Generated from Smithy shape ``com.amazonaws.connect#VocabularySummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.vocabulary_summary

VocabularySummaryList: TypeAlias = list[
    "capo_connect.types.vocabulary_summary.VocabularySummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: VocabularySummaryList) -> list:
    import capo_connect.types.vocabulary_summary

    out: list = []
    for item in value:
        out.append(capo_connect.types.vocabulary_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> VocabularySummaryList:
    import capo_connect.types.vocabulary_summary

    out: VocabularySummaryList = []
    for item in data:
        out.append(capo_connect.types.vocabulary_summary.deserialize_json(item))
    return out
