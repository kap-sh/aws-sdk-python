"""Generated from Smithy shape ``com.amazonaws.mediaconvert#MxfXavcDurationMode``."""

from typing import Literal, TypeAlias, cast

"""To create an output that complies with the XAVC file format guidelines for interoperability, keep the default value, Drop frames for compliance. To include all frames from your input in this output, keep the default setting, Allow any duration. The number of frames that MediaConvert excludes when you set this to Drop frames for compliance depends on the output frame rate and duration."""
MxfXavcDurationMode: TypeAlias = Literal[
    "ALLOW_ANY_DURATION",
    "DROP_FRAMES_FOR_COMPLIANCE",
]


# --- restJson1 ser/de ---
def serialize_json(value: MxfXavcDurationMode) -> str:
    return value


def deserialize_json(data: str) -> MxfXavcDurationMode:
    return cast(MxfXavcDurationMode, data)
