"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ResourceContentType``."""

from typing import Literal, TypeAlias, cast

ResourceContentType: TypeAlias = Literal[
    "EMAIL",
    "PHONE_NUMBER",
    "LINK",
    "OTHER",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceContentType) -> str:
    return value


def deserialize_json(data: str) -> ResourceContentType:
    return cast(ResourceContentType, data)
