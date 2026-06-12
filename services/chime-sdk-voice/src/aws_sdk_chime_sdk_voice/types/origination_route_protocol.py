"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#OriginationRouteProtocol``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_voice.errors import DeserializationError

OriginationRouteProtocol: TypeAlias = Literal[
    "TCP",
    "UDP",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TCP",
        "UDP",
    )
)


def serialize_json(value: OriginationRouteProtocol) -> str:
    return value


def deserialize_json(data: str) -> OriginationRouteProtocol:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OriginationRouteProtocol value: {data!r}")
    return cast(OriginationRouteProtocol, data)
