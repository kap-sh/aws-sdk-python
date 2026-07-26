"""Generated from Smithy shape ``com.amazonaws.sagemaker#InstancePoolSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.instance_pool_summary

InstancePoolSummaryList: TypeAlias = list[
    "capo_sagemaker.types.instance_pool_summary.InstancePoolSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstancePoolSummaryList) -> list:
    import capo_sagemaker.types.instance_pool_summary

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.instance_pool_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InstancePoolSummaryList:
    import capo_sagemaker.types.instance_pool_summary

    out: InstancePoolSummaryList = []
    for item in data:
        out.append(
            capo_sagemaker.types.instance_pool_summary.deserialize_aws_json_1_1(item)
        )
    return out
