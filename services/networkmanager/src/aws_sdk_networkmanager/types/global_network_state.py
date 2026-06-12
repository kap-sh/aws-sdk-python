"""Generated from Smithy shape ``com.amazonaws.networkmanager#GlobalNetworkState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_networkmanager.errors import DeserializationError

GlobalNetworkState: TypeAlias = Literal[
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


def serialize_json(value: GlobalNetworkState) -> str:
    return value


def deserialize_json(data: str) -> GlobalNetworkState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GlobalNetworkState value: {data!r}")
    return cast(GlobalNetworkState, data)
