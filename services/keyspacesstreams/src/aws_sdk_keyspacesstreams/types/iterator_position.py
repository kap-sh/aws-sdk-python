"""Generated from Smithy shape ``com.amazonaws.keyspacesstreams#IteratorPosition``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_keyspacesstreams.errors import DeserializationError
from aws_sdk_keyspacesstreams._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

IteratorPosition: TypeAlias = Literal["AT_TIP", "BEHIND_TIP",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("AT_TIP", "BEHIND_TIP",))


def serialize_aws_json_1_0(value: IteratorPosition) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IteratorPosition:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IteratorPosition value: {data!r}")
    return cast(IteratorPosition, data)