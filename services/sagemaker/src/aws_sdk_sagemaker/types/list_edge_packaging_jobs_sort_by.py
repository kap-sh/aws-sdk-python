"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListEdgePackagingJobsSortBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ListEdgePackagingJobsSortBy: TypeAlias = Literal[
    "NAME",
    "MODEL_NAME",
    "CREATION_TIME",
    "LAST_MODIFIED_TIME",
    "STATUS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NAME",
        "MODEL_NAME",
        "CREATION_TIME",
        "LAST_MODIFIED_TIME",
        "STATUS",
    )
)


def serialize_aws_json_1_1(value: ListEdgePackagingJobsSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ListEdgePackagingJobsSortBy:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ListEdgePackagingJobsSortBy value: {data!r}"
        )
    return cast(ListEdgePackagingJobsSortBy, data)
