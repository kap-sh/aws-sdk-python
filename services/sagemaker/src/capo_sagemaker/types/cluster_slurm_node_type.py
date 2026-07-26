"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterSlurmNodeType``."""

from typing import Literal, TypeAlias, cast

ClusterSlurmNodeType: TypeAlias = Literal[
    "Controller",
    "Login",
    "Compute",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterSlurmNodeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterSlurmNodeType:
    return cast(ClusterSlurmNodeType, data)
