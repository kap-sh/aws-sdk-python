"""Generated from Smithy shape ``com.amazonaws.neptunedata#Format``."""

from typing import Literal, TypeAlias, cast

Format: TypeAlias = Literal[
    "csv",
    "opencypher",
    "ntriples",
    "nquads",
    "rdfxml",
    "turtle",
]


# --- restJson1 ser/de ---
def serialize_json(value: Format) -> str:
    return value


def deserialize_json(data: str) -> Format:
    return cast(Format, data)
