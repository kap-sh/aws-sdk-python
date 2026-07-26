"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DeinterlacerControl``."""

from typing import Literal, TypeAlias, cast

"""- When set to NORMAL (default), the deinterlacer does not convert frames that are tagged in metadata as progressive. It will only convert those that are tagged as some other type. - When set to FORCE_ALL_FRAMES, the deinterlacer converts every frame to progressive - even those that are already tagged as progressive. Turn Force mode on only if there is a good chance that the metadata has tagged frames as progressive when they are not progressive. Do not turn on otherwise; processing frames that are already progressive into progressive will probably result in lower quality video."""
DeinterlacerControl: TypeAlias = Literal[
    "FORCE_ALL_FRAMES",
    "NORMAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: DeinterlacerControl) -> str:
    return value


def deserialize_json(data: str) -> DeinterlacerControl:
    return cast(DeinterlacerControl, data)
