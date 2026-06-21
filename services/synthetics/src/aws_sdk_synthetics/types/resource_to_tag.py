"""Generated from Smithy shape ``com.amazonaws.synthetics#ResourceToTag``."""

from typing import Literal, TypeAlias, cast

ResourceToTag: TypeAlias = Literal["lambda-function",]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceToTag) -> str:
    return value


def deserialize_json(data: str) -> ResourceToTag:
    return cast(ResourceToTag, data)
