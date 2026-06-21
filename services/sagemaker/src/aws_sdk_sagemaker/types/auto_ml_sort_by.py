"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLSortBy``."""

from typing import Literal, TypeAlias, cast

AutoMLSortBy: TypeAlias = Literal[
    "Name",
    "CreationTime",
    "Status",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoMLSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutoMLSortBy:
    return cast(AutoMLSortBy, data)
