"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ColorMetadata``."""

from typing import Literal, TypeAlias, cast

"""Choose Insert for this setting to include color metadata in this output. Choose Ignore to exclude color metadata from this output. If you don't specify a value, the service sets this to Insert by default."""
ColorMetadata: TypeAlias = Literal[
    "IGNORE",
    "INSERT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ColorMetadata) -> str:
    return value


def deserialize_json(data: str) -> ColorMetadata:
    return cast(ColorMetadata, data)
