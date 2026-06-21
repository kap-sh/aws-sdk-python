"""Generated from Smithy shape ``com.amazonaws.quicksight#RefreshFailureAlertStatus``."""

from typing import Literal, TypeAlias, cast

RefreshFailureAlertStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: RefreshFailureAlertStatus) -> str:
    return value


def deserialize_json(data: str) -> RefreshFailureAlertStatus:
    return cast(RefreshFailureAlertStatus, data)
