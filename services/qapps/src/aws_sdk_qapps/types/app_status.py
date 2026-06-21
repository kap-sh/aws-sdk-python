"""Generated from Smithy shape ``com.amazonaws.qapps#AppStatus``."""

from typing import Literal, TypeAlias, cast

AppStatus: TypeAlias = Literal[
    "PUBLISHED",
    "DRAFT",
    "DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AppStatus) -> str:
    return value


def deserialize_json(data: str) -> AppStatus:
    return cast(AppStatus, data)
