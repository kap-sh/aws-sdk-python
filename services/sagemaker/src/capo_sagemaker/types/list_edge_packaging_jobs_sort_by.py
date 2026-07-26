"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListEdgePackagingJobsSortBy``."""

from typing import Literal, TypeAlias, cast

ListEdgePackagingJobsSortBy: TypeAlias = Literal[
    "NAME",
    "MODEL_NAME",
    "CREATION_TIME",
    "LAST_MODIFIED_TIME",
    "STATUS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEdgePackagingJobsSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ListEdgePackagingJobsSortBy:
    return cast(ListEdgePackagingJobsSortBy, data)
