"""Generated from Smithy shape ``com.amazonaws.sagemaker#SortQuotaBy``."""

from typing import Literal, TypeAlias, cast

SortQuotaBy: TypeAlias = Literal[
    "Name",
    "CreationTime",
    "Status",
    "ClusterArn",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SortQuotaBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SortQuotaBy:
    return cast(SortQuotaBy, data)
