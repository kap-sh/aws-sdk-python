"""Generated from Smithy shape ``com.amazonaws.sagemaker#ResourceSharingStrategy``."""

from typing import Literal, TypeAlias, cast

ResourceSharingStrategy: TypeAlias = Literal[
    "Lend",
    "DontLend",
    "LendAndBorrow",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceSharingStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceSharingStrategy:
    return cast(ResourceSharingStrategy, data)
