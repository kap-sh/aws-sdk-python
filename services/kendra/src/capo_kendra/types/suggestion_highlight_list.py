"""Generated from Smithy shape ``com.amazonaws.kendra#SuggestionHighlightList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.suggestion_highlight

SuggestionHighlightList: TypeAlias = list[
    "capo_kendra.types.suggestion_highlight.SuggestionHighlight"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SuggestionHighlightList) -> list:
    import capo_kendra.types.suggestion_highlight

    out: list = []
    for item in value:
        out.append(capo_kendra.types.suggestion_highlight.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SuggestionHighlightList:
    import capo_kendra.types.suggestion_highlight

    out: SuggestionHighlightList = []
    for item in data:
        out.append(
            capo_kendra.types.suggestion_highlight.deserialize_aws_json_1_1(item)
        )
    return out
