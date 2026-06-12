"""Generated from Smithy shape ``com.amazonaws.sagemaker#ComputeQuotaResourceConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.compute_quota_resource_config

ComputeQuotaResourceConfigList: TypeAlias = list[
    "aws_sdk_sagemaker.types.compute_quota_resource_config.ComputeQuotaResourceConfig"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComputeQuotaResourceConfigList) -> list:
    import aws_sdk_sagemaker.types.compute_quota_resource_config

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.compute_quota_resource_config.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ComputeQuotaResourceConfigList:
    import aws_sdk_sagemaker.types.compute_quota_resource_config

    out: ComputeQuotaResourceConfigList = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.compute_quota_resource_config.deserialize_aws_json_1_1(
                item
            )
        )
    return out
