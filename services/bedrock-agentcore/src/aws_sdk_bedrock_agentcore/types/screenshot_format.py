"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ScreenshotFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore.errors import DeserializationError

"""<p>The image format for a browser screenshot.</p>"""
ScreenshotFormat: TypeAlias = Literal["PNG",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("PNG",))


def serialize_json(value: ScreenshotFormat) -> str:
    return value


def deserialize_json(data: str) -> ScreenshotFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScreenshotFormat value: {data!r}")
    return cast(ScreenshotFormat, data)
