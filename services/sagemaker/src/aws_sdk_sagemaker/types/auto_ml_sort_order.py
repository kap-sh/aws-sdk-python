"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLSortOrder``."""

from typing import Literal, TypeAlias, cast

AutoMLSortOrder: TypeAlias = Literal[
    "Ascending",
    "Descending",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoMLSortOrder) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutoMLSortOrder:
    return cast(AutoMLSortOrder, data)
