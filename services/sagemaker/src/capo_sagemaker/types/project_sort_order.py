"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProjectSortOrder``."""

from typing import Literal, TypeAlias, cast

ProjectSortOrder: TypeAlias = Literal[
    "Ascending",
    "Descending",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProjectSortOrder) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProjectSortOrder:
    return cast(ProjectSortOrder, data)
