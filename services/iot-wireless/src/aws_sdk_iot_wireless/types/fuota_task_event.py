"""Generated from Smithy shape ``com.amazonaws.iotwireless#FuotaTaskEvent``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_wireless.errors import DeserializationError

"""<p>The event for a log message, if the log message is tied to a FUOTA task.</p>"""
FuotaTaskEvent: TypeAlias = Literal["Fuota",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Fuota",))


def serialize_json(value: FuotaTaskEvent) -> str:
    return value


def deserialize_json(data: str) -> FuotaTaskEvent:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FuotaTaskEvent value: {data!r}")
    return cast(FuotaTaskEvent, data)
