"""Generated from Smithy shape ``com.amazonaws.outposts#OutpostGeneration``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_outposts.errors import DeserializationError

OutpostGeneration: TypeAlias = Literal[
    "GENERATION_2",
    "GENERATION_1",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GENERATION_2",
        "GENERATION_1",
    )
)


def serialize_json(value: OutpostGeneration) -> str:
    return value


def deserialize_json(data: str) -> OutpostGeneration:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OutpostGeneration value: {data!r}")
    return cast(OutpostGeneration, data)
