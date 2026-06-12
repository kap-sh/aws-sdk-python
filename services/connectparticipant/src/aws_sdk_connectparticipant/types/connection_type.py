"""Generated from Smithy shape ``com.amazonaws.connectparticipant#ConnectionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connectparticipant.errors import DeserializationError

ConnectionType: TypeAlias = Literal[
    "WEBSOCKET",
    "CONNECTION_CREDENTIALS",
    "WEBRTC_CONNECTION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "WEBSOCKET",
        "CONNECTION_CREDENTIALS",
        "WEBRTC_CONNECTION",
    )
)


def serialize_json(value: ConnectionType) -> str:
    return value


def deserialize_json(data: str) -> ConnectionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectionType value: {data!r}")
    return cast(ConnectionType, data)
