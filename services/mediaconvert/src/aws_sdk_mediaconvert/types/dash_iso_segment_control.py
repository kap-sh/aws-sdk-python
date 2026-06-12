"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DashIsoSegmentControl``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""When set to SINGLE_FILE, a single output file is generated, which is internally segmented using the Fragment Length and Segment Length. When set to SEGMENTED_FILES, separate segment files will be created."""
DashIsoSegmentControl: TypeAlias = Literal[
    "SINGLE_FILE",
    "SEGMENTED_FILES",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SINGLE_FILE",
        "SEGMENTED_FILES",
    )
)


def serialize_json(value: DashIsoSegmentControl) -> str:
    return value


def deserialize_json(data: str) -> DashIsoSegmentControl:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DashIsoSegmentControl value: {data!r}")
    return cast(DashIsoSegmentControl, data)
