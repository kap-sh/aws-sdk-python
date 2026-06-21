"""Generated from Smithy shape ``com.amazonaws.quicksight#WidgetStatus``."""

from typing import Literal, TypeAlias, cast

WidgetStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: WidgetStatus) -> str:
    return value


def deserialize_json(data: str) -> WidgetStatus:
    return cast(WidgetStatus, data)
