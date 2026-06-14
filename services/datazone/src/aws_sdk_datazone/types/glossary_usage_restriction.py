"""Generated from Smithy shape ``com.amazonaws.datazone#GlossaryUsageRestriction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

GlossaryUsageRestriction: TypeAlias = Literal["ASSET_GOVERNED_TERMS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ASSET_GOVERNED_TERMS",))


def serialize_json(value: GlossaryUsageRestriction) -> str:
    return value


def deserialize_json(data: str) -> GlossaryUsageRestriction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GlossaryUsageRestriction value: {data!r}")
    return cast(GlossaryUsageRestriction, data)
