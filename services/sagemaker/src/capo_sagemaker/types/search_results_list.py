"""Generated from Smithy shape ``com.amazonaws.sagemaker#SearchResultsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.search_record

SearchResultsList: TypeAlias = list["capo_sagemaker.types.search_record.SearchRecord"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchResultsList) -> list:
    import capo_sagemaker.types.search_record

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.search_record.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SearchResultsList:
    import capo_sagemaker.types.search_record

    out: SearchResultsList = []
    for item in data:
        out.append(capo_sagemaker.types.search_record.deserialize_aws_json_1_1(item))
    return out
