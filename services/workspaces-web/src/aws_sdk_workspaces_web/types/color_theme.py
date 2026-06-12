"""Generated from Smithy shape ``com.amazonaws.workspacesweb#ColorTheme``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_workspaces_web.errors import DeserializationError
from aws_sdk_workspaces_web._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ColorTheme: TypeAlias = Literal["Light", "Dark",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Light", "Dark",))


def serialize_json(value: ColorTheme) -> str:
    return value


def deserialize_json(data: str) -> ColorTheme:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ColorTheme value: {data!r}")
    return cast(ColorTheme, data)