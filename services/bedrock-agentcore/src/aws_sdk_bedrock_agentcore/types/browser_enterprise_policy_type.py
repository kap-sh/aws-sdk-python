"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#BrowserEnterprisePolicyType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agentcore.errors import DeserializationError
from aws_sdk_bedrock_agentcore._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""<p>The type of browser enterprise policy. Available values are <code>MANAGED</code> and <code>RECOMMENDED</code>.</p>"""
BrowserEnterprisePolicyType: TypeAlias = Literal["MANAGED", "RECOMMENDED",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("MANAGED", "RECOMMENDED",))


def serialize_json(value: BrowserEnterprisePolicyType) -> str:
    return value


def deserialize_json(data: str) -> BrowserEnterprisePolicyType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BrowserEnterprisePolicyType value: {data!r}")
    return cast(BrowserEnterprisePolicyType, data)