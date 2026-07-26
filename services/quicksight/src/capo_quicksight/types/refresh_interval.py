"""Generated from Smithy shape ``com.amazonaws.quicksight#RefreshInterval``."""

from typing import Literal, TypeAlias, cast

RefreshInterval: TypeAlias = Literal[
    "MINUTE15",
    "MINUTE30",
    "HOURLY",
    "DAILY",
    "WEEKLY",
    "MONTHLY",
]


# --- restJson1 ser/de ---
def serialize_json(value: RefreshInterval) -> str:
    return value


def deserialize_json(data: str) -> RefreshInterval:
    return cast(RefreshInterval, data)
