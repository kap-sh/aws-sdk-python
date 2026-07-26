"""Generated from Smithy shape ``com.amazonaws.rtbfabric#LinkDirection``."""

from typing import Literal, TypeAlias, cast

LinkDirection: TypeAlias = Literal[
    "RESPONSE",
    "REQUEST",
]


# --- restJson1 ser/de ---
def serialize_json(value: LinkDirection) -> str:
    return value


def deserialize_json(data: str) -> LinkDirection:
    return cast(LinkDirection, data)
