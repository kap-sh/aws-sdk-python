"""Generated from Smithy shape ``com.amazonaws.sagemaker#RecommendationJobVpcSecurityGroupIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.recommendation_job_vpc_security_group_id

RecommendationJobVpcSecurityGroupIds: TypeAlias = list[
    "aws_sdk_sagemaker.types.recommendation_job_vpc_security_group_id.RecommendationJobVpcSecurityGroupId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecommendationJobVpcSecurityGroupIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> RecommendationJobVpcSecurityGroupIds:
    return list(data)
