"""Generated from Smithy shape ``com.amazonaws.sagemaker#SortExperimentsBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

SortExperimentsBy: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: SortExperimentsBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SortExperimentsBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SortExperimentsBy value: {data!r}")
    return cast(SortExperimentsBy, data)
