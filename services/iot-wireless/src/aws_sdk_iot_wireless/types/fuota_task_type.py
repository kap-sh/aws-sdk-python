"""Generated from Smithy shape ``com.amazonaws.iotwireless#FuotaTaskType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_wireless.errors import DeserializationError

"""<p>The FUOTA task type.</p>"""
FuotaTaskType: TypeAlias = Literal["LoRaWAN",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("LoRaWAN",))


def serialize_json(value: FuotaTaskType) -> str:
    return value


def deserialize_json(data: str) -> FuotaTaskType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FuotaTaskType value: {data!r}")
    return cast(FuotaTaskType, data)
