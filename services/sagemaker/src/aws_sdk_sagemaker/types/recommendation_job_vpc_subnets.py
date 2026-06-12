"""Generated from Smithy shape ``com.amazonaws.sagemaker#RecommendationJobVpcSubnets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.recommendation_job_vpc_subnet_id

RecommendationJobVpcSubnets: TypeAlias = list[
    "aws_sdk_sagemaker.types.recommendation_job_vpc_subnet_id.RecommendationJobVpcSubnetId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecommendationJobVpcSubnets) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> RecommendationJobVpcSubnets:
    return list(data)
