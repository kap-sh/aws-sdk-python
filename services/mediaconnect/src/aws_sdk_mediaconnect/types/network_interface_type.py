"""Generated from Smithy shape ``com.amazonaws.mediaconnect#NetworkInterfaceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

NetworkInterfaceType: TypeAlias = Literal[
    "ena",
    "efa",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ena",
        "efa",
    )
)


def serialize_json(value: NetworkInterfaceType) -> str:
    return value


def deserialize_json(data: str) -> NetworkInterfaceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NetworkInterfaceType value: {data!r}")
    return cast(NetworkInterfaceType, data)
