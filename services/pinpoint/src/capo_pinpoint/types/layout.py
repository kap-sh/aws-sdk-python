"""Generated from Smithy shape ``com.amazonaws.pinpoint#Layout``."""

from typing import Literal, TypeAlias, cast

Layout: TypeAlias = Literal[
    "BOTTOM_BANNER",
    "TOP_BANNER",
    "OVERLAYS",
    "MOBILE_FEED",
    "MIDDLE_BANNER",
    "CAROUSEL",
]


# --- restJson1 ser/de ---
def serialize_json(value: Layout) -> str:
    return value


def deserialize_json(data: str) -> Layout:
    return cast(Layout, data)
