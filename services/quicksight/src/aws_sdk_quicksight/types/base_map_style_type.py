"""Generated from Smithy shape ``com.amazonaws.quicksight#BaseMapStyleType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

BaseMapStyleType: TypeAlias = Literal[
    "LIGHT_GRAY",
    "DARK_GRAY",
    "STREET",
    "IMAGERY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LIGHT_GRAY",
        "DARK_GRAY",
        "STREET",
        "IMAGERY",
    )
)


def serialize_json(value: BaseMapStyleType) -> str:
    return value


def deserialize_json(data: str) -> BaseMapStyleType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BaseMapStyleType value: {data!r}")
    return cast(BaseMapStyleType, data)
