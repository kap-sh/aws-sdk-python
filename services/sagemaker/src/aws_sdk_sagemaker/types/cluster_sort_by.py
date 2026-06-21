"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterSortBy``."""

from typing import Literal, TypeAlias, cast

ClusterSortBy: TypeAlias = Literal[
    "CREATION_TIME",
    "NAME",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterSortBy:
    return cast(ClusterSortBy, data)
