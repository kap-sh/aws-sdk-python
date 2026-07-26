"""Generated from Smithy shape ``com.amazonaws.sagemaker#SortClusterSchedulerConfigBy``."""

from typing import Literal, TypeAlias, cast

SortClusterSchedulerConfigBy: TypeAlias = Literal[
    "Name",
    "CreationTime",
    "Status",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SortClusterSchedulerConfigBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SortClusterSchedulerConfigBy:
    return cast(SortClusterSchedulerConfigBy, data)
