"""Generated from Smithy shape ``com.amazonaws.bedrock#SortModelsBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

SortModelsBy: TypeAlias = Literal["CreationTime",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CreationTime",))


def serialize_json(value: SortModelsBy) -> str:
    return value


def deserialize_json(data: str) -> SortModelsBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SortModelsBy value: {data!r}")
    return cast(SortModelsBy, data)
