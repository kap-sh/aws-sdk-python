"""Generated from Smithy shape ``com.amazonaws.quicksight#StarburstProductType``."""

from typing import Literal, TypeAlias, cast

StarburstProductType: TypeAlias = Literal[
    "GALAXY",
    "ENTERPRISE",
]


# --- restJson1 ser/de ---
def serialize_json(value: StarburstProductType) -> str:
    return value


def deserialize_json(data: str) -> StarburstProductType:
    return cast(StarburstProductType, data)
