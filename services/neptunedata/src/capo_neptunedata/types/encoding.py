"""Generated from Smithy shape ``com.amazonaws.neptunedata#Encoding``."""

from typing import Literal, TypeAlias, cast

Encoding: TypeAlias = Literal["gzip",]


# --- restJson1 ser/de ---
def serialize_json(value: Encoding) -> str:
    return value


def deserialize_json(data: str) -> Encoding:
    return cast(Encoding, data)
