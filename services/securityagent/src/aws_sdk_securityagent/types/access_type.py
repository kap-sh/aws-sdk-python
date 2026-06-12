"""Generated from Smithy shape ``com.amazonaws.securityagent#AccessType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_securityagent.errors import DeserializationError
from aws_sdk_securityagent._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""<p>Defines the visibility level of provider resources. PRIVATE indicates restricted access, while PUBLIC indicates open access.</p>"""
AccessType: TypeAlias = Literal["PRIVATE", "PUBLIC",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("PRIVATE", "PUBLIC",))


def serialize_json(value: AccessType) -> str:
    return value


def deserialize_json(data: str) -> AccessType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AccessType value: {data!r}")
    return cast(AccessType, data)