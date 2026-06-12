"""Generated from Smithy shape ``com.amazonaws.sagemaker#SortContextsBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

SortContextsBy: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: SortContextsBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SortContextsBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SortContextsBy value: {data!r}")
    return cast(SortContextsBy, data)
