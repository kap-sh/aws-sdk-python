"""Generated from Smithy shape ``com.amazonaws.odb#Access``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_odb.errors import DeserializationError
from aws_sdk_odb._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

Access: TypeAlias = Literal["ENABLED", "DISABLED",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("ENABLED", "DISABLED",))


def serialize_aws_json_1_0(value: Access) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Access:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Access value: {data!r}")
    return cast(Access, data)