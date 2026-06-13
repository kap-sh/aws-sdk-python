"""Generated from Smithy shape ``com.amazonaws.neptunedata#Format``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_neptunedata.errors import DeserializationError

Format: TypeAlias = Literal[
    "csv",
    "opencypher",
    "ntriples",
    "nquads",
    "rdfxml",
    "turtle",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "csv",
        "opencypher",
        "ntriples",
        "nquads",
        "rdfxml",
        "turtle",
    )
)


def serialize_json(value: Format) -> str:
    return value


def deserialize_json(data: str) -> Format:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Format value: {data!r}")
    return cast(Format, data)
