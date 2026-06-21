"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#PreviewStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>Represents the preview status.</p>"""
PreviewStatus: TypeAlias = Literal[
    "PREVIEW_IN_PROGRESS",
    "PREVIEW_FAILED",
    "PREVIEW_READY",
]


# --- restJson1 ser/de ---
def serialize_json(value: PreviewStatus) -> str:
    return value


def deserialize_json(data: str) -> PreviewStatus:
    return cast(PreviewStatus, data)
