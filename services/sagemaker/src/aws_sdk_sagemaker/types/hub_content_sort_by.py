"""Generated from Smithy shape ``com.amazonaws.sagemaker#HubContentSortBy``."""

from typing import Literal, TypeAlias, cast

HubContentSortBy: TypeAlias = Literal[
    "HubContentName",
    "CreationTime",
    "HubContentStatus",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HubContentSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HubContentSortBy:
    return cast(HubContentSortBy, data)
