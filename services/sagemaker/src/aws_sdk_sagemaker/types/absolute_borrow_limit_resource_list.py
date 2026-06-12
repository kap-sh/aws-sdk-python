"""Generated from Smithy shape ``com.amazonaws.sagemaker#AbsoluteBorrowLimitResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.compute_quota_resource_config

AbsoluteBorrowLimitResourceList: TypeAlias = list[
    "aws_sdk_sagemaker.types.compute_quota_resource_config.ComputeQuotaResourceConfig"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AbsoluteBorrowLimitResourceList) -> list:
    import aws_sdk_sagemaker.types.compute_quota_resource_config

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.compute_quota_resource_config.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AbsoluteBorrowLimitResourceList:
    import aws_sdk_sagemaker.types.compute_quota_resource_config

    out: AbsoluteBorrowLimitResourceList = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.compute_quota_resource_config.deserialize_aws_json_1_1(
                item
            )
        )
    return out
