"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#ContentResolution``."""

from typing import Literal, TypeAlias, cast

ContentResolution: TypeAlias = Literal[
    "None",
    "FHD",
    "UHD",
]


# --- restJson1 ser/de ---
def serialize_json(value: ContentResolution) -> str:
    return value


def deserialize_json(data: str) -> ContentResolution:
    return cast(ContentResolution, data)
