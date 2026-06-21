"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AdvancedInputFilterAddTexture``."""

from typing import Literal, TypeAlias, cast

"""Add texture and detail to areas of your input video content that were lost after applying the Advanced input filter. To adaptively add texture and reduce softness: Choose Enabled. To not add any texture: Keep the default value, Disabled. We recommend that you choose Disabled for input video content that doesn't have texture, including screen recordings, computer graphics, or cartoons."""
AdvancedInputFilterAddTexture: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AdvancedInputFilterAddTexture) -> str:
    return value


def deserialize_json(data: str) -> AdvancedInputFilterAddTexture:
    return cast(AdvancedInputFilterAddTexture, data)
