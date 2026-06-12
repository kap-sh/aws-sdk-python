"""Generated from Smithy shape ``com.amazonaws.customerprofiles#Unit``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

Unit: TypeAlias = Literal["DAYS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("DAYS",))


def serialize_json(value: Unit) -> str:
    return value


def deserialize_json(data: str) -> Unit:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Unit value: {data!r}")
    return cast(Unit, data)
