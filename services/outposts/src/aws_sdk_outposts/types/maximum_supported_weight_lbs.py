"""Generated from Smithy shape ``com.amazonaws.outposts#MaximumSupportedWeightLbs``."""

from typing import Literal, TypeAlias, cast

MaximumSupportedWeightLbs: TypeAlias = Literal[
    "NO_LIMIT",
    "MAX_1400_LBS",
    "MAX_1600_LBS",
    "MAX_1800_LBS",
    "MAX_2000_LBS",
]


# --- restJson1 ser/de ---
def serialize_json(value: MaximumSupportedWeightLbs) -> str:
    return value


def deserialize_json(data: str) -> MaximumSupportedWeightLbs:
    return cast(MaximumSupportedWeightLbs, data)
