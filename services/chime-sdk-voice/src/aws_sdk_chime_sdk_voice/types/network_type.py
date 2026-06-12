"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#NetworkType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_voice.errors import DeserializationError

NetworkType: TypeAlias = Literal[
    "IPV4_ONLY",
    "DUAL_STACK",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IPV4_ONLY",
        "DUAL_STACK",
    )
)


def serialize_json(value: NetworkType) -> str:
    return value


def deserialize_json(data: str) -> NetworkType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NetworkType value: {data!r}")
    return cast(NetworkType, data)
