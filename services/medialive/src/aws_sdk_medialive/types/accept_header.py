"""Generated from Smithy shape ``com.amazonaws.medialive#AcceptHeader``."""

from typing import Literal, TypeAlias, cast

"""The HTTP Accept header. Indicates the requested type fothe thumbnail."""
AcceptHeader: TypeAlias = Literal["image/jpeg",]


# --- restJson1 ser/de ---
def serialize_json(value: AcceptHeader) -> str:
    return value


def deserialize_json(data: str) -> AcceptHeader:
    return cast(AcceptHeader, data)
