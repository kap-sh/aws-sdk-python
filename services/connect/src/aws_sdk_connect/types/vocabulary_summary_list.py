"""Generated from Smithy shape ``com.amazonaws.connect#VocabularySummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.vocabulary_summary

VocabularySummaryList: TypeAlias = list[
    "aws_sdk_connect.types.vocabulary_summary.VocabularySummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: VocabularySummaryList) -> list:
    import aws_sdk_connect.types.vocabulary_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.vocabulary_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> VocabularySummaryList:
    import aws_sdk_connect.types.vocabulary_summary

    out: VocabularySummaryList = []
    for item in data:
        out.append(aws_sdk_connect.types.vocabulary_summary.deserialize_json(item))
    return out
