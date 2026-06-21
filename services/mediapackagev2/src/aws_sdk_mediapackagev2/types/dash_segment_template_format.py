"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#DashSegmentTemplateFormat``."""

from typing import Literal, TypeAlias, cast

DashSegmentTemplateFormat: TypeAlias = Literal["NUMBER_WITH_TIMELINE",]


# --- restJson1 ser/de ---
def serialize_json(value: DashSegmentTemplateFormat) -> str:
    return value


def deserialize_json(data: str) -> DashSegmentTemplateFormat:
    return cast(DashSegmentTemplateFormat, data)
