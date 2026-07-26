"""Generated from Smithy shape ``com.amazonaws.mediapackage#SegmentTemplateFormat``."""

from typing import Literal, TypeAlias, cast

SegmentTemplateFormat: TypeAlias = Literal[
    "NUMBER_WITH_TIMELINE",
    "TIME_WITH_TIMELINE",
    "NUMBER_WITH_DURATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: SegmentTemplateFormat) -> str:
    return value


def deserialize_json(data: str) -> SegmentTemplateFormat:
    return cast(SegmentTemplateFormat, data)
