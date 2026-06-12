"""Generated from Smithy shape ``com.amazonaws.networkmanager#CoreNetworkPolicyAlias``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_networkmanager.errors import DeserializationError

CoreNetworkPolicyAlias: TypeAlias = Literal[
    "LIVE",
    "LATEST",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LIVE",
        "LATEST",
    )
)


def serialize_json(value: CoreNetworkPolicyAlias) -> str:
    return value


def deserialize_json(data: str) -> CoreNetworkPolicyAlias:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CoreNetworkPolicyAlias value: {data!r}")
    return cast(CoreNetworkPolicyAlias, data)
