"""Generated from Smithy shape ``com.amazonaws.sagemaker#HubSortBy``."""

from typing import Literal, TypeAlias, cast

HubSortBy: TypeAlias = Literal[
    "HubName",
    "CreationTime",
    "HubStatus",
    "AccountIdOwner",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HubSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HubSortBy:
    return cast(HubSortBy, data)
