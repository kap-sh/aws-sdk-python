"""Generated from Smithy shape ``com.amazonaws.groundstation#EphemerisSource``."""

from typing import Literal, TypeAlias, cast

EphemerisSource: TypeAlias = Literal[
    "CUSTOMER_PROVIDED",
    "SPACE_TRACK",
]


# --- restJson1 ser/de ---
def serialize_json(value: EphemerisSource) -> str:
    return value


def deserialize_json(data: str) -> EphemerisSource:
    return cast(EphemerisSource, data)
