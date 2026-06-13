"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#BrowserProfileStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
from aws_sdk_bedrock_agentcore_control._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""<p>The status of a browser profile.</p>"""
BrowserProfileStatus: TypeAlias = Literal["READY", "DELETING", "DELETED", "SAVING",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("READY", "DELETING", "DELETED", "SAVING",))


def serialize_json(value: BrowserProfileStatus) -> str:
    return value


def deserialize_json(data: str) -> BrowserProfileStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BrowserProfileStatus value: {data!r}")
    return cast(BrowserProfileStatus, data)