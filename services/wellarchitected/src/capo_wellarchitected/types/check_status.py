"""Generated from Smithy shape ``com.amazonaws.wellarchitected#CheckStatus``."""

from typing import Literal, TypeAlias, cast

CheckStatus: TypeAlias = Literal[
    "OKAY",
    "WARNING",
    "ERROR",
    "NOT_AVAILABLE",
    "FETCH_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: CheckStatus) -> str:
    return value


def deserialize_json(data: str) -> CheckStatus:
    return cast(CheckStatus, data)
