"""Generated from Smithy shape ``com.amazonaws.connecthealth#Specialty``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connecthealth.errors import DeserializationError

Specialty: TypeAlias = Literal["PRIMARY_CARE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("PRIMARY_CARE",))


def serialize_json(value: Specialty) -> str:
    return value


def deserialize_json(data: str) -> Specialty:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Specialty value: {data!r}")
    return cast(Specialty, data)
