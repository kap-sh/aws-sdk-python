"""Generated from Smithy shape ``com.amazonaws.mediatailor#AdMarkupType``."""

from typing import Literal, TypeAlias, cast

AdMarkupType: TypeAlias = Literal[
    "DATERANGE",
    "SCTE35_ENHANCED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AdMarkupType) -> str:
    return value


def deserialize_json(data: str) -> AdMarkupType:
    return cast(AdMarkupType, data)
