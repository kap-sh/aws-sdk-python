"""Generated from Smithy shape ``com.amazonaws.kendra#SuggestionTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.suggestion_type

SuggestionTypes: TypeAlias = list["aws_sdk_kendra.types.suggestion_type.SuggestionType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SuggestionTypes) -> list:
    import aws_sdk_kendra.types.suggestion_type

    out: list = []
    for item in value:
        out.append(aws_sdk_kendra.types.suggestion_type.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SuggestionTypes:
    import aws_sdk_kendra.types.suggestion_type

    out: SuggestionTypes = []
    for item in data:
        out.append(aws_sdk_kendra.types.suggestion_type.deserialize_aws_json_1_1(item))
    return out
