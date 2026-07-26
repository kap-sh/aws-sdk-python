"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#FragmentSelectorType``."""

from typing import Literal, TypeAlias, cast

FragmentSelectorType: TypeAlias = Literal[
    "ProducerTimestamp",
    "ServerTimestamp",
]


# --- restJson1 ser/de ---
def serialize_json(value: FragmentSelectorType) -> str:
    return value


def deserialize_json(data: str) -> FragmentSelectorType:
    return cast(FragmentSelectorType, data)
