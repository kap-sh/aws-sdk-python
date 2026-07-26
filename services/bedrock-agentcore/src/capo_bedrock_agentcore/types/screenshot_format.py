"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ScreenshotFormat``."""

from typing import Literal, TypeAlias, cast

"""<p>The image format for a browser screenshot.</p>"""
ScreenshotFormat: TypeAlias = Literal["PNG",]


# --- restJson1 ser/de ---
def serialize_json(value: ScreenshotFormat) -> str:
    return value


def deserialize_json(data: str) -> ScreenshotFormat:
    return cast(ScreenshotFormat, data)
