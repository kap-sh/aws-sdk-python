"""Generated from Smithy shape ``com.amazonaws.quicksight#SmallMultiplesAxisPlacement``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

SmallMultiplesAxisPlacement: TypeAlias = Literal[
    "OUTSIDE",
    "INSIDE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OUTSIDE",
        "INSIDE",
    )
)


def serialize_json(value: SmallMultiplesAxisPlacement) -> str:
    return value


def deserialize_json(data: str) -> SmallMultiplesAxisPlacement:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SmallMultiplesAxisPlacement value: {data!r}"
        )
    return cast(SmallMultiplesAxisPlacement, data)
