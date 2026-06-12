"""Generated from Smithy shape ``com.amazonaws.ssm#NodeTypeName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

NodeTypeName: TypeAlias = Literal["Instance",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Instance",))


def serialize_aws_json_1_1(value: NodeTypeName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NodeTypeName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NodeTypeName value: {data!r}")
    return cast(NodeTypeName, data)
