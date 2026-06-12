"""Generated from Smithy shape ``com.amazonaws.iot#AbortAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

AbortAction: TypeAlias = Literal["CANCEL",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CANCEL",))


def serialize_json(value: AbortAction) -> str:
    return value


def deserialize_json(data: str) -> AbortAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AbortAction value: {data!r}")
    return cast(AbortAction, data)
