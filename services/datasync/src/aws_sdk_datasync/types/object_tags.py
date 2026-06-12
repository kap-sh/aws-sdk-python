"""Generated from Smithy shape ``com.amazonaws.datasync#ObjectTags``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datasync.errors import DeserializationError

ObjectTags: TypeAlias = Literal[
    "PRESERVE",
    "NONE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PRESERVE",
        "NONE",
    )
)


def serialize_aws_json_1_1(value: ObjectTags) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ObjectTags:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ObjectTags value: {data!r}")
    return cast(ObjectTags, data)
