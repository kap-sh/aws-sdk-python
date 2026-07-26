"""Generated from Smithy shape ``com.amazonaws.sagemaker#NestedFiltersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.nested_filters

NestedFiltersList: TypeAlias = list["capo_sagemaker.types.nested_filters.NestedFilters"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NestedFiltersList) -> list:
    import capo_sagemaker.types.nested_filters

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.nested_filters.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> NestedFiltersList:
    import capo_sagemaker.types.nested_filters

    out: NestedFiltersList = []
    for item in data:
        out.append(capo_sagemaker.types.nested_filters.deserialize_aws_json_1_1(item))
    return out
