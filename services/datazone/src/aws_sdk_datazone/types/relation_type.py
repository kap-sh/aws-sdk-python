"""Generated from Smithy shape ``com.amazonaws.datazone#RelationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

RelationType: TypeAlias = Literal["LINEAGE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("LINEAGE",))


def serialize_json(value: RelationType) -> str:
    return value


def deserialize_json(data: str) -> RelationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RelationType value: {data!r}")
    return cast(RelationType, data)
