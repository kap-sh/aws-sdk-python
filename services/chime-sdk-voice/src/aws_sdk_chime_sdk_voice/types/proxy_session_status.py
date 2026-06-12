"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#ProxySessionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_voice.errors import DeserializationError

ProxySessionStatus: TypeAlias = Literal[
    "Open",
    "InProgress",
    "Closed",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Open",
        "InProgress",
        "Closed",
    )
)


def serialize_json(value: ProxySessionStatus) -> str:
    return value


def deserialize_json(data: str) -> ProxySessionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProxySessionStatus value: {data!r}")
    return cast(ProxySessionStatus, data)
