"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#ClusterDeploymentType``."""

from typing import Literal, TypeAlias, cast

ClusterDeploymentType: TypeAlias = Literal["MULTI_NODE_READ_REPLICAS",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ClusterDeploymentType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ClusterDeploymentType:
    return cast(ClusterDeploymentType, data)
