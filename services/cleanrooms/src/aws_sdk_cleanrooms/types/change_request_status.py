"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ChangeRequestStatus``."""

from typing import Literal, TypeAlias, cast

ChangeRequestStatus: TypeAlias = Literal[
    "PENDING",
    "APPROVED",
    "CANCELLED",
    "DENIED",
    "COMMITTED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ChangeRequestStatus) -> str:
    return value


def deserialize_json(data: str) -> ChangeRequestStatus:
    return cast(ChangeRequestStatus, data)
