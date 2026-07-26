"""Generated from Smithy shape ``com.amazonaws.sagemaker#FilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.filter

FilterList: TypeAlias = list["capo_sagemaker.types.filter.Filter"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilterList) -> list:
    import capo_sagemaker.types.filter

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FilterList:
    import capo_sagemaker.types.filter

    out: FilterList = []
    for item in data:
        out.append(capo_sagemaker.types.filter.deserialize_aws_json_1_1(item))
    return out
