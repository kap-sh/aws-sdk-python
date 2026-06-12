"""Generated from Smithy shape ``com.amazonaws.greengrassv2#IoTJobAbortAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_greengrassv2.errors import DeserializationError

IoTJobAbortAction: TypeAlias = Literal["CANCEL",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CANCEL",))


def serialize_json(value: IoTJobAbortAction) -> str:
    return value


def deserialize_json(data: str) -> IoTJobAbortAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IoTJobAbortAction value: {data!r}")
    return cast(IoTJobAbortAction, data)
