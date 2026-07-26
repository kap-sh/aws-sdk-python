"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DisassociatedDataStorageState``."""

from typing import Literal, TypeAlias, cast

DisassociatedDataStorageState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DisassociatedDataStorageState) -> str:
    return value


def deserialize_json(data: str) -> DisassociatedDataStorageState:
    return cast(DisassociatedDataStorageState, data)
