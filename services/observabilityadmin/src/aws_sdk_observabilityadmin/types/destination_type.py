"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#DestinationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_observabilityadmin.errors import DeserializationError

DestinationType: TypeAlias = Literal["cloud-watch-logs",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("cloud-watch-logs",))


def serialize_json(value: DestinationType) -> str:
    return value


def deserialize_json(data: str) -> DestinationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DestinationType value: {data!r}")
    return cast(DestinationType, data)
