"""Generated from Smithy shape ``com.amazonaws.datasync#ObjectVersionIds``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datasync.errors import DeserializationError

ObjectVersionIds: TypeAlias = Literal[
    "INCLUDE",
    "NONE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INCLUDE",
        "NONE",
    )
)


def serialize_aws_json_1_1(value: ObjectVersionIds) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ObjectVersionIds:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ObjectVersionIds value: {data!r}")
    return cast(ObjectVersionIds, data)
