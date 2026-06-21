"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListCompilationJobsSortBy``."""

from typing import Literal, TypeAlias, cast

ListCompilationJobsSortBy: TypeAlias = Literal[
    "Name",
    "CreationTime",
    "Status",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCompilationJobsSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ListCompilationJobsSortBy:
    return cast(ListCompilationJobsSortBy, data)
