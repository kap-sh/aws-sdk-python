"""Generated from Smithy shape ``com.amazonaws.datasync#TaskFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datasync.errors import DeserializationError

TaskFilterName: TypeAlias = Literal[
    "LocationId",
    "CreationTime",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LocationId",
        "CreationTime",
    )
)


def serialize_aws_json_1_1(value: TaskFilterName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TaskFilterName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TaskFilterName value: {data!r}")
    return cast(TaskFilterName, data)
