"""Generated from Smithy shape ``com.amazonaws.translate#ParallelDataStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_translate.errors import DeserializationError

ParallelDataStatus: TypeAlias = Literal[
    "CREATING",
    "UPDATING",
    "ACTIVE",
    "DELETING",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "UPDATING",
        "ACTIVE",
        "DELETING",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: ParallelDataStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ParallelDataStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ParallelDataStatus value: {data!r}")
    return cast(ParallelDataStatus, data)
