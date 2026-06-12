"""Generated from Smithy shape ``com.amazonaws.workspaces#InternetFallbackProtocol``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_workspaces.errors import DeserializationError
from aws_sdk_workspaces._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

InternetFallbackProtocol: TypeAlias = Literal["PCOIP",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("PCOIP",))


def serialize_aws_json_1_1(value: InternetFallbackProtocol) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InternetFallbackProtocol:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InternetFallbackProtocol value: {data!r}")
    return cast(InternetFallbackProtocol, data)
