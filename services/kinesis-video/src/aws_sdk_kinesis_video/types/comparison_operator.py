"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#ComparisonOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis_video.errors import DeserializationError

ComparisonOperator: TypeAlias = Literal["BEGINS_WITH",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("BEGINS_WITH",))


def serialize_json(value: ComparisonOperator) -> str:
    return value


def deserialize_json(data: str) -> ComparisonOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ComparisonOperator value: {data!r}")
    return cast(ComparisonOperator, data)
