"""Generated from Smithy shape ``com.amazonaws.sagemaker#PropertyNameSuggestionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.property_name_suggestion

PropertyNameSuggestionList: TypeAlias = list[
    "capo_sagemaker.types.property_name_suggestion.PropertyNameSuggestion"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PropertyNameSuggestionList) -> list:
    import capo_sagemaker.types.property_name_suggestion

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.property_name_suggestion.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PropertyNameSuggestionList:
    import capo_sagemaker.types.property_name_suggestion

    out: PropertyNameSuggestionList = []
    for item in data:
        out.append(
            capo_sagemaker.types.property_name_suggestion.deserialize_aws_json_1_1(item)
        )
    return out
