"""Generated from Smithy shape ``com.amazonaws.sagemaker#SearchResultsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.search_record

SearchResultsList: TypeAlias = list[
    "aws_sdk_sagemaker.types.search_record.SearchRecord"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchResultsList) -> list:
    import aws_sdk_sagemaker.types.search_record

    out: list = []
    for item in value:
        out.append(aws_sdk_sagemaker.types.search_record.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SearchResultsList:
    import aws_sdk_sagemaker.types.search_record

    out: SearchResultsList = []
    for item in data:
        out.append(aws_sdk_sagemaker.types.search_record.deserialize_aws_json_1_1(item))
    return out
