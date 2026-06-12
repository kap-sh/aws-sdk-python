"""Generated from Smithy shape ``com.amazonaws.glue#LogicalOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

LogicalOperator: TypeAlias = Literal["EQUALS",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("EQUALS",))


def serialize_aws_json_1_1(value: LogicalOperator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LogicalOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LogicalOperator value: {data!r}")
    return cast(LogicalOperator, data)
