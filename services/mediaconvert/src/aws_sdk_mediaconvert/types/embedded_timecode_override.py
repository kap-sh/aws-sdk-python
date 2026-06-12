"""Generated from Smithy shape ``com.amazonaws.mediaconvert#EmbeddedTimecodeOverride``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Set Embedded timecode override to Use MDPM when your AVCHD input contains timecode tag data in the Modified Digital Video Pack Metadata. When you do, we recommend you also set Timecode source to Embedded. Leave Embedded timecode override blank, or set to None, when your input does not contain MDPM timecode."""
EmbeddedTimecodeOverride: TypeAlias = Literal[
    "NONE",
    "USE_MDPM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "USE_MDPM",
    )
)


def serialize_json(value: EmbeddedTimecodeOverride) -> str:
    return value


def deserialize_json(data: str) -> EmbeddedTimecodeOverride:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EmbeddedTimecodeOverride value: {data!r}")
    return cast(EmbeddedTimecodeOverride, data)
