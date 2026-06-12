"""Generated from Smithy shape ``com.amazonaws.medialive#OfferingType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Offering type, e.g. 'NO_UPFRONT'"""
OfferingType: TypeAlias = Literal["NO_UPFRONT",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("NO_UPFRONT",))


def serialize_json(value: OfferingType) -> str:
    return value


def deserialize_json(data: str) -> OfferingType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OfferingType value: {data!r}")
    return cast(OfferingType, data)
