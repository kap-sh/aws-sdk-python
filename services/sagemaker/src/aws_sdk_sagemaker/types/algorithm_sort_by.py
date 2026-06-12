"""Generated from Smithy shape ``com.amazonaws.sagemaker#AlgorithmSortBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

AlgorithmSortBy: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: AlgorithmSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AlgorithmSortBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AlgorithmSortBy value: {data!r}")
    return cast(AlgorithmSortBy, data)
