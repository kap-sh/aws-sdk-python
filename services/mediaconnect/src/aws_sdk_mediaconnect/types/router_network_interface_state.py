"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterNetworkInterfaceState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

RouterNetworkInterfaceState: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "UPDATING",
    "DELETING",
    "ERROR",
    "RECOVERING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "ACTIVE",
        "UPDATING",
        "DELETING",
        "ERROR",
        "RECOVERING",
    )
)


def serialize_json(value: RouterNetworkInterfaceState) -> str:
    return value


def deserialize_json(data: str) -> RouterNetworkInterfaceState:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RouterNetworkInterfaceState value: {data!r}"
        )
    return cast(RouterNetworkInterfaceState, data)
