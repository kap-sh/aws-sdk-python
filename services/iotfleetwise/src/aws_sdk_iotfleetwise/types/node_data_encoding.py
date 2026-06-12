"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#NodeDataEncoding``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotfleetwise.errors import DeserializationError

NodeDataEncoding: TypeAlias = Literal[
    "BINARY",
    "TYPED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BINARY",
        "TYPED",
    )
)


def serialize_aws_json_1_0(value: NodeDataEncoding) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> NodeDataEncoding:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NodeDataEncoding value: {data!r}")
    return cast(NodeDataEncoding, data)
