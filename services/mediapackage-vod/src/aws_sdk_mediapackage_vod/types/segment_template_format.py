"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#SegmentTemplateFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediapackage_vod.errors import DeserializationError

SegmentTemplateFormat: TypeAlias = Literal[
    "NUMBER_WITH_TIMELINE",
    "TIME_WITH_TIMELINE",
    "NUMBER_WITH_DURATION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NUMBER_WITH_TIMELINE",
        "TIME_WITH_TIMELINE",
        "NUMBER_WITH_DURATION",
    )
)


def serialize_json(value: SegmentTemplateFormat) -> str:
    return value


def deserialize_json(data: str) -> SegmentTemplateFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SegmentTemplateFormat value: {data!r}")
    return cast(SegmentTemplateFormat, data)
