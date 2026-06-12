"""Generated from Smithy shape ``com.amazonaws.databrew#OrderedBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_databrew.errors import DeserializationError

OrderedBy: TypeAlias = Literal["LAST_MODIFIED_DATE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("LAST_MODIFIED_DATE",))


def serialize_json(value: OrderedBy) -> str:
    return value


def deserialize_json(data: str) -> OrderedBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OrderedBy value: {data!r}")
    return cast(OrderedBy, data)
