"""Generated from Smithy shape ``com.amazonaws.outposts#PowerDrawKva``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_outposts.errors import DeserializationError

PowerDrawKva: TypeAlias = Literal[
    "POWER_5_KVA",
    "POWER_10_KVA",
    "POWER_15_KVA",
    "POWER_30_KVA",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "POWER_5_KVA",
        "POWER_10_KVA",
        "POWER_15_KVA",
        "POWER_30_KVA",
    )
)


def serialize_json(value: PowerDrawKva) -> str:
    return value


def deserialize_json(data: str) -> PowerDrawKva:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PowerDrawKva value: {data!r}")
    return cast(PowerDrawKva, data)
