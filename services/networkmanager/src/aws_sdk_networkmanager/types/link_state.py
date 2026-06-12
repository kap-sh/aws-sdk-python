"""Generated from Smithy shape ``com.amazonaws.networkmanager#LinkState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_networkmanager.errors import DeserializationError

LinkState: TypeAlias = Literal[
    "PENDING",
    "AVAILABLE",
    "DELETING",
    "UPDATING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "AVAILABLE",
        "DELETING",
        "UPDATING",
    )
)


def serialize_json(value: LinkState) -> str:
    return value


def deserialize_json(data: str) -> LinkState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LinkState value: {data!r}")
    return cast(LinkState, data)
