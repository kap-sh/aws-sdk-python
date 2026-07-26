"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AacSpecification``."""

from typing import Literal, TypeAlias, cast

"""Use MPEG-2 AAC instead of MPEG-4 AAC audio for raw or MPEG-2 Transport Stream containers."""
AacSpecification: TypeAlias = Literal[
    "MPEG2",
    "MPEG4",
]


# --- restJson1 ser/de ---
def serialize_json(value: AacSpecification) -> str:
    return value


def deserialize_json(data: str) -> AacSpecification:
    return cast(AacSpecification, data)
