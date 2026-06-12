"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListAIWorkloadConfigsSortBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ListAIWorkloadConfigsSortBy: TypeAlias = Literal[
    "Name",
    "CreationTime",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Name",
        "CreationTime",
    )
)


def serialize_aws_json_1_1(value: ListAIWorkloadConfigsSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ListAIWorkloadConfigsSortBy:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ListAIWorkloadConfigsSortBy value: {data!r}"
        )
    return cast(ListAIWorkloadConfigsSortBy, data)
