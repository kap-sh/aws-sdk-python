"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DashIsoSegmentControl``."""

from typing import Literal, TypeAlias, cast

"""When set to SINGLE_FILE, a single output file is generated, which is internally segmented using the Fragment Length and Segment Length. When set to SEGMENTED_FILES, separate segment files will be created."""
DashIsoSegmentControl: TypeAlias = Literal[
    "SINGLE_FILE",
    "SEGMENTED_FILES",
]


# --- restJson1 ser/de ---
def serialize_json(value: DashIsoSegmentControl) -> str:
    return value


def deserialize_json(data: str) -> DashIsoSegmentControl:
    return cast(DashIsoSegmentControl, data)
