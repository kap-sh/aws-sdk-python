"""Generated from Smithy shape ``com.amazonaws.memorydb#SourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_memorydb.errors import DeserializationError

SourceType: TypeAlias = Literal[
    "node",
    "parameter-group",
    "subnet-group",
    "cluster",
    "user",
    "acl",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "node",
        "parameter-group",
        "subnet-group",
        "cluster",
        "user",
        "acl",
    )
)


def serialize_aws_json_1_1(value: SourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SourceType value: {data!r}")
    return cast(SourceType, data)
