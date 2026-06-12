"""Generated from Smithy shape ``com.amazonaws.outposts#MaximumSupportedWeightLbs``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_outposts.errors import DeserializationError

MaximumSupportedWeightLbs: TypeAlias = Literal[
    "NO_LIMIT",
    "MAX_1400_LBS",
    "MAX_1600_LBS",
    "MAX_1800_LBS",
    "MAX_2000_LBS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NO_LIMIT",
        "MAX_1400_LBS",
        "MAX_1600_LBS",
        "MAX_1800_LBS",
        "MAX_2000_LBS",
    )
)


def serialize_json(value: MaximumSupportedWeightLbs) -> str:
    return value


def deserialize_json(data: str) -> MaximumSupportedWeightLbs:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MaximumSupportedWeightLbs value: {data!r}")
    return cast(MaximumSupportedWeightLbs, data)
