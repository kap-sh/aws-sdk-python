"""Generated from Smithy shape ``com.amazonaws.kendra#SuggestionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.suggestion

SuggestionList: TypeAlias = list["capo_kendra.types.suggestion.Suggestion"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SuggestionList) -> list:
    import capo_kendra.types.suggestion

    out: list = []
    for item in value:
        out.append(capo_kendra.types.suggestion.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SuggestionList:
    import capo_kendra.types.suggestion

    out: SuggestionList = []
    for item in data:
        out.append(capo_kendra.types.suggestion.deserialize_aws_json_1_1(item))
    return out
