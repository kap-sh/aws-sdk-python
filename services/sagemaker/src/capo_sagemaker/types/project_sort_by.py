"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProjectSortBy``."""

from typing import Literal, TypeAlias, cast

ProjectSortBy: TypeAlias = Literal[
    "Name",
    "CreationTime",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProjectSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProjectSortBy:
    return cast(ProjectSortBy, data)
