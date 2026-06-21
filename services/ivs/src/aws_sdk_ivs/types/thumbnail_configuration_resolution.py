"""Generated from Smithy shape ``com.amazonaws.ivs#ThumbnailConfigurationResolution``."""

from typing import Literal, TypeAlias, cast

ThumbnailConfigurationResolution: TypeAlias = Literal[
    "SD",
    "HD",
    "FULL_HD",
    "LOWEST_RESOLUTION",
]


# --- restJson1 ser/de ---
def serialize_json(value: ThumbnailConfigurationResolution) -> str:
    return value


def deserialize_json(data: str) -> ThumbnailConfigurationResolution:
    return cast(ThumbnailConfigurationResolution, data)
