"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterSlurmConfigStrategy``."""

from typing import Literal, TypeAlias, cast

ClusterSlurmConfigStrategy: TypeAlias = Literal[
    "Overwrite",
    "Managed",
    "Merge",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterSlurmConfigStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterSlurmConfigStrategy:
    return cast(ClusterSlurmConfigStrategy, data)
