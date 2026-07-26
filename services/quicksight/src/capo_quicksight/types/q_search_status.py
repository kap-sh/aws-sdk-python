"""Generated from Smithy shape ``com.amazonaws.quicksight#QSearchStatus``."""

from typing import Literal, TypeAlias, cast

QSearchStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: QSearchStatus) -> str:
    return value


def deserialize_json(data: str) -> QSearchStatus:
    return cast(QSearchStatus, data)
