"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#PreviewStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_apigatewayv2.errors import DeserializationError

"""<p>Represents the preview status.</p>"""
PreviewStatus: TypeAlias = Literal[
    "PREVIEW_IN_PROGRESS",
    "PREVIEW_FAILED",
    "PREVIEW_READY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PREVIEW_IN_PROGRESS",
        "PREVIEW_FAILED",
        "PREVIEW_READY",
    )
)


def serialize_json(value: PreviewStatus) -> str:
    return value


def deserialize_json(data: str) -> PreviewStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PreviewStatus value: {data!r}")
    return cast(PreviewStatus, data)
