"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#Currency``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agentcore.errors import DeserializationError
from aws_sdk_bedrock_agentcore._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""<p>Supported currency codes.</p>"""
Currency: TypeAlias = Literal["USD",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("USD",))


def serialize_json(value: Currency) -> str:
    return value


def deserialize_json(data: str) -> Currency:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Currency value: {data!r}")
    return cast(Currency, data)