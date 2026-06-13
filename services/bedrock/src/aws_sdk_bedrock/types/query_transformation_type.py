"""Generated from Smithy shape ``com.amazonaws.bedrock#QueryTransformationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

QueryTransformationType: TypeAlias = Literal["QUERY_DECOMPOSITION",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("QUERY_DECOMPOSITION",))


def serialize_json(value: QueryTransformationType) -> str:
    return value


def deserialize_json(data: str) -> QueryTransformationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QueryTransformationType value: {data!r}")
    return cast(QueryTransformationType, data)
