"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#PreviewStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_apigatewayv2.errors import DeserializationError
from aws_sdk_apigatewayv2._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

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
