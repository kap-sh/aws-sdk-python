"""Generated from Smithy shape ``com.amazonaws.sagemaker#SortActionsBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

SortActionsBy: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: SortActionsBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SortActionsBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SortActionsBy value: {data!r}")
    return cast(SortActionsBy, data)
