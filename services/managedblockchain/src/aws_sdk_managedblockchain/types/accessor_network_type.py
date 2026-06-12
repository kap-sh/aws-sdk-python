"""Generated from Smithy shape ``com.amazonaws.managedblockchain#AccessorNetworkType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_managedblockchain.errors import DeserializationError

AccessorNetworkType: TypeAlias = Literal[
    "ETHEREUM_GOERLI",
    "ETHEREUM_MAINNET",
    "ETHEREUM_MAINNET_AND_GOERLI",
    "POLYGON_MAINNET",
    "POLYGON_MUMBAI",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ETHEREUM_GOERLI",
        "ETHEREUM_MAINNET",
        "ETHEREUM_MAINNET_AND_GOERLI",
        "POLYGON_MAINNET",
        "POLYGON_MUMBAI",
    )
)


def serialize_json(value: AccessorNetworkType) -> str:
    return value


def deserialize_json(data: str) -> AccessorNetworkType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AccessorNetworkType value: {data!r}")
    return cast(AccessorNetworkType, data)
