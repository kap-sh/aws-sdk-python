"""Generated from Smithy shape ``com.amazonaws.networkmanager#CoreNetworkState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_networkmanager.errors import DeserializationError

CoreNetworkState: TypeAlias = Literal[
    "CREATING",
    "UPDATING",
    "AVAILABLE",
    "DELETING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "UPDATING",
        "AVAILABLE",
        "DELETING",
    )
)


def serialize_json(value: CoreNetworkState) -> str:
    return value


def deserialize_json(data: str) -> CoreNetworkState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CoreNetworkState value: {data!r}")
    return cast(CoreNetworkState, data)
