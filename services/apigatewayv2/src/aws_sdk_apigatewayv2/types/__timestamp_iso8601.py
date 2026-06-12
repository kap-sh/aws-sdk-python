"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#__timestampIso8601``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_apigatewayv2.errors import DeserializationError
from aws_sdk_apigatewayv2._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

__timestampIso8601: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: __timestampIso8601) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> __timestampIso8601:
    return datetime.datetime.fromisoformat(data)
