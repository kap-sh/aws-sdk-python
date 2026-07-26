"""Generated from Smithy shape ``com.amazonaws.quicksight#KPIVisualStandardLayoutType``."""

from typing import Literal, TypeAlias, cast

KPIVisualStandardLayoutType: TypeAlias = Literal[
    "CLASSIC",
    "VERTICAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: KPIVisualStandardLayoutType) -> str:
    return value


def deserialize_json(data: str) -> KPIVisualStandardLayoutType:
    return cast(KPIVisualStandardLayoutType, data)
