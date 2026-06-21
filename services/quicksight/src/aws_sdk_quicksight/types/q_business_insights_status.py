"""Generated from Smithy shape ``com.amazonaws.quicksight#QBusinessInsightsStatus``."""

from typing import Literal, TypeAlias, cast

QBusinessInsightsStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: QBusinessInsightsStatus) -> str:
    return value


def deserialize_json(data: str) -> QBusinessInsightsStatus:
    return cast(QBusinessInsightsStatus, data)
