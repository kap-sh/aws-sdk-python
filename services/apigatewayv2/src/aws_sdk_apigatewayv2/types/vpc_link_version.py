"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#VpcLinkVersion``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_apigatewayv2.errors import DeserializationError
from aws_sdk_apigatewayv2._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""<p>The version of the VPC link.</p>"""
VpcLinkVersion: TypeAlias = Literal["V2",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("V2",))


def serialize_json(value: VpcLinkVersion) -> str:
    return value


def deserialize_json(data: str) -> VpcLinkVersion:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VpcLinkVersion value: {data!r}")
    return cast(VpcLinkVersion, data)
