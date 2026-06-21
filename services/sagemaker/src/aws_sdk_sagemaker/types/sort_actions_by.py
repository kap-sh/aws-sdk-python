"""Generated from Smithy shape ``com.amazonaws.sagemaker#SortActionsBy``."""

from typing import Literal, TypeAlias, cast

SortActionsBy: TypeAlias = Literal[
    "Name",
    "CreationTime",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SortActionsBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SortActionsBy:
    return cast(SortActionsBy, data)
