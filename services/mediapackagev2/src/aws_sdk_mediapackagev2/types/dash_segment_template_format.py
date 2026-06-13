"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#DashSegmentTemplateFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediapackagev2.errors import DeserializationError

DashSegmentTemplateFormat: TypeAlias = Literal["NUMBER_WITH_TIMELINE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("NUMBER_WITH_TIMELINE",))


def serialize_json(value: DashSegmentTemplateFormat) -> str:
    return value


def deserialize_json(data: str) -> DashSegmentTemplateFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DashSegmentTemplateFormat value: {data!r}")
    return cast(DashSegmentTemplateFormat, data)
