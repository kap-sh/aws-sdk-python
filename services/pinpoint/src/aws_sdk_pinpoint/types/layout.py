"""Generated from Smithy shape ``com.amazonaws.pinpoint#Layout``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pinpoint.errors import DeserializationError

Layout: TypeAlias = Literal[
    "BOTTOM_BANNER",
    "TOP_BANNER",
    "OVERLAYS",
    "MOBILE_FEED",
    "MIDDLE_BANNER",
    "CAROUSEL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BOTTOM_BANNER",
        "TOP_BANNER",
        "OVERLAYS",
        "MOBILE_FEED",
        "MIDDLE_BANNER",
        "CAROUSEL",
    )
)


def serialize_json(value: Layout) -> str:
    return value


def deserialize_json(data: str) -> Layout:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Layout value: {data!r}")
    return cast(Layout, data)
