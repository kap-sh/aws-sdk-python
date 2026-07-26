"""Generated from Smithy shape ``com.amazonaws.batch#QuotaShareStatus``."""

from typing import Literal, TypeAlias, cast

QuotaShareStatus: TypeAlias = Literal[
    "CREATING",
    "VALID",
    "INVALID",
    "UPDATING",
    "DELETING",
]


# --- restJson1 ser/de ---
def serialize_json(value: QuotaShareStatus) -> str:
    return value


def deserialize_json(data: str) -> QuotaShareStatus:
    return cast(QuotaShareStatus, data)
