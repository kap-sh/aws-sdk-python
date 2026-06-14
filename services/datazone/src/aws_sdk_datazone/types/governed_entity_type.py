"""Generated from Smithy shape ``com.amazonaws.datazone#GovernedEntityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

GovernedEntityType: TypeAlias = Literal["ASSET",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ASSET",))


def serialize_json(value: GovernedEntityType) -> str:
    return value


def deserialize_json(data: str) -> GovernedEntityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GovernedEntityType value: {data!r}")
    return cast(GovernedEntityType, data)
