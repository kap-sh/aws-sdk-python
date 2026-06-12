"""Generated from Smithy shape ``com.amazonaws.ssm#NodeAggregatorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

NodeAggregatorType: TypeAlias = Literal["Count",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Count",))


def serialize_aws_json_1_1(value: NodeAggregatorType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NodeAggregatorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NodeAggregatorType value: {data!r}")
    return cast(NodeAggregatorType, data)
