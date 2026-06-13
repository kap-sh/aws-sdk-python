"""Generated from Smithy shape ``com.amazonaws.quicksight#StarburstProductType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

StarburstProductType: TypeAlias = Literal[
    "GALAXY",
    "ENTERPRISE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GALAXY",
        "ENTERPRISE",
    )
)


def serialize_json(value: StarburstProductType) -> str:
    return value


def deserialize_json(data: str) -> StarburstProductType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StarburstProductType value: {data!r}")
    return cast(StarburstProductType, data)
