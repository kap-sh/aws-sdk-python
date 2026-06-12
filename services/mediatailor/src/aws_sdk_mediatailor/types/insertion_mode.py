"""Generated from Smithy shape ``com.amazonaws.mediatailor#InsertionMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediatailor.errors import DeserializationError

"""<p>Insertion Mode controls whether players can use stitched or guided ad insertion.</p>"""
InsertionMode: TypeAlias = Literal[
    "STITCHED_ONLY",
    "PLAYER_SELECT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STITCHED_ONLY",
        "PLAYER_SELECT",
    )
)


def serialize_json(value: InsertionMode) -> str:
    return value


def deserialize_json(data: str) -> InsertionMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InsertionMode value: {data!r}")
    return cast(InsertionMode, data)
