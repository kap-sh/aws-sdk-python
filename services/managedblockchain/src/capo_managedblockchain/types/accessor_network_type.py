"""Generated from Smithy shape ``com.amazonaws.managedblockchain#AccessorNetworkType``."""

from typing import Literal, TypeAlias, cast

AccessorNetworkType: TypeAlias = Literal[
    "ETHEREUM_GOERLI",
    "ETHEREUM_MAINNET",
    "ETHEREUM_MAINNET_AND_GOERLI",
    "POLYGON_MAINNET",
    "POLYGON_MUMBAI",
]


# --- restJson1 ser/de ---
def serialize_json(value: AccessorNetworkType) -> str:
    return value


def deserialize_json(data: str) -> AccessorNetworkType:
    return cast(AccessorNetworkType, data)
