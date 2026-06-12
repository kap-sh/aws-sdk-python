"""Generated from Smithy shape ``com.amazonaws.connect#SlaType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

SlaType: TypeAlias = Literal["CaseField",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CaseField",))


def serialize_json(value: SlaType) -> str:
    return value


def deserialize_json(data: str) -> SlaType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SlaType value: {data!r}")
    return cast(SlaType, data)
