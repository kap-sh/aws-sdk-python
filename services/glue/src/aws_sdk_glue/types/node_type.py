"""Generated from Smithy shape ``com.amazonaws.glue#NodeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

NodeType: TypeAlias = Literal[
    "CRAWLER",
    "JOB",
    "TRIGGER",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CRAWLER",
        "JOB",
        "TRIGGER",
    )
)


def serialize_aws_json_1_1(value: NodeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NodeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NodeType value: {data!r}")
    return cast(NodeType, data)
