"""Generated from Smithy shape ``com.amazonaws.managedblockchain#Framework``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_managedblockchain.errors import DeserializationError

Framework: TypeAlias = Literal[
    "HYPERLEDGER_FABRIC",
    "ETHEREUM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HYPERLEDGER_FABRIC",
        "ETHEREUM",
    )
)


def serialize_json(value: Framework) -> str:
    return value


def deserialize_json(data: str) -> Framework:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Framework value: {data!r}")
    return cast(Framework, data)
