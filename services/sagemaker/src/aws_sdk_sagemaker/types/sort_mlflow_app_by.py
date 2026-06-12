"""Generated from Smithy shape ``com.amazonaws.sagemaker#SortMlflowAppBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

SortMlflowAppBy: TypeAlias = Literal[
    "Name",
    "CreationTime",
    "Status",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Name",
        "CreationTime",
        "Status",
    )
)


def serialize_aws_json_1_1(value: SortMlflowAppBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SortMlflowAppBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SortMlflowAppBy value: {data!r}")
    return cast(SortMlflowAppBy, data)
