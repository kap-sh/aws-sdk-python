"""Generated from Smithy shape ``com.amazonaws.managedblockchain#Framework``."""

from typing import Literal, TypeAlias, cast

Framework: TypeAlias = Literal[
    "HYPERLEDGER_FABRIC",
    "ETHEREUM",
]


# --- restJson1 ser/de ---
def serialize_json(value: Framework) -> str:
    return value


def deserialize_json(data: str) -> Framework:
    return cast(Framework, data)
