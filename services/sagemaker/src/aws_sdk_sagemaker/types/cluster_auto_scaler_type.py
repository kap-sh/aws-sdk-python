"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterAutoScalerType``."""

from typing import Literal, TypeAlias, cast

ClusterAutoScalerType: TypeAlias = Literal["Karpenter",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterAutoScalerType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterAutoScalerType:
    return cast(ClusterAutoScalerType, data)
