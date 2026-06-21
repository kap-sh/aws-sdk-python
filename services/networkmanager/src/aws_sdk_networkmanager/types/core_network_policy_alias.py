"""Generated from Smithy shape ``com.amazonaws.networkmanager#CoreNetworkPolicyAlias``."""

from typing import Literal, TypeAlias, cast

CoreNetworkPolicyAlias: TypeAlias = Literal[
    "LIVE",
    "LATEST",
]


# --- restJson1 ser/de ---
def serialize_json(value: CoreNetworkPolicyAlias) -> str:
    return value


def deserialize_json(data: str) -> CoreNetworkPolicyAlias:
    return cast(CoreNetworkPolicyAlias, data)
