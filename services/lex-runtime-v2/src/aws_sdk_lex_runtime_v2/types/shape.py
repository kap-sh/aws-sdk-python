"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#Shape``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_runtime_v2.errors import DeserializationError

Shape: TypeAlias = Literal[
    "Scalar",
    "List",
    "Composite",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Scalar",
        "List",
        "Composite",
    )
)


def serialize_json(value: Shape) -> str:
    return value


def deserialize_json(data: str) -> Shape:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Shape value: {data!r}")
    return cast(Shape, data)
