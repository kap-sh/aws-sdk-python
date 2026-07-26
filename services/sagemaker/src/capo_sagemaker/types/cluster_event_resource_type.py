"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterEventResourceType``."""

from typing import Literal, TypeAlias, cast

ClusterEventResourceType: TypeAlias = Literal[
    "Cluster",
    "InstanceGroup",
    "Instance",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterEventResourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterEventResourceType:
    return cast(ClusterEventResourceType, data)
