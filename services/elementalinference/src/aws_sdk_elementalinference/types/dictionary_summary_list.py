"""Generated from Smithy shape ``com.amazonaws.elementalinference#DictionarySummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_elementalinference.types.dictionary_summary

DictionarySummaryList: TypeAlias = list[
    "aws_sdk_elementalinference.types.dictionary_summary.DictionarySummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DictionarySummaryList) -> list:
    import aws_sdk_elementalinference.types.dictionary_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_elementalinference.types.dictionary_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DictionarySummaryList:
    import aws_sdk_elementalinference.types.dictionary_summary

    out: DictionarySummaryList = []
    for item in data:
        out.append(
            aws_sdk_elementalinference.types.dictionary_summary.deserialize_json(item)
        )
    return out
