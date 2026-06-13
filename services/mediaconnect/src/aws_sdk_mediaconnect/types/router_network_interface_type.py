"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterNetworkInterfaceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

RouterNetworkInterfaceType: TypeAlias = Literal[
    "PUBLIC",
    "VPC",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PUBLIC",
        "VPC",
    )
)


def serialize_json(value: RouterNetworkInterfaceType) -> str:
    return value


def deserialize_json(data: str) -> RouterNetworkInterfaceType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RouterNetworkInterfaceType value: {data!r}"
        )
    return cast(RouterNetworkInterfaceType, data)
