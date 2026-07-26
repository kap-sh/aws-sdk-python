"""Generated from Smithy shape ``com.amazonaws.lexruntimeservice#ConfirmationStatus``."""

from typing import Literal, TypeAlias, cast

ConfirmationStatus: TypeAlias = Literal[
    "None",
    "Confirmed",
    "Denied",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfirmationStatus) -> str:
    return value


def deserialize_json(data: str) -> ConfirmationStatus:
    return cast(ConfirmationStatus, data)
