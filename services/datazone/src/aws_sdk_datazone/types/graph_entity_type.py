"""Generated from Smithy shape ``com.amazonaws.datazone#GraphEntityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

GraphEntityType: TypeAlias = Literal["LINEAGE_NODE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("LINEAGE_NODE",))


def serialize_json(value: GraphEntityType) -> str:
    return value


def deserialize_json(data: str) -> GraphEntityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GraphEntityType value: {data!r}")
    return cast(GraphEntityType, data)
