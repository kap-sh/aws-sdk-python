"""Generated from Smithy shape ``com.amazonaws.resiliencehub#DisruptionType``."""

from typing import Literal, TypeAlias, cast

DisruptionType: TypeAlias = Literal[
    "Software",
    "Hardware",
    "AZ",
    "Region",
]


# --- restJson1 ser/de ---
def serialize_json(value: DisruptionType) -> str:
    return value


def deserialize_json(data: str) -> DisruptionType:
    return cast(DisruptionType, data)
