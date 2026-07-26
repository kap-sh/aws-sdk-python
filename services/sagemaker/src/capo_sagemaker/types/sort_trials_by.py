"""Generated from Smithy shape ``com.amazonaws.sagemaker#SortTrialsBy``."""

from typing import Literal, TypeAlias, cast

SortTrialsBy: TypeAlias = Literal[
    "Name",
    "CreationTime",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SortTrialsBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SortTrialsBy:
    return cast(SortTrialsBy, data)
