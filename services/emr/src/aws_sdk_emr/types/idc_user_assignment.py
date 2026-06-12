"""Generated from Smithy shape ``com.amazonaws.emr#IdcUserAssignment``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_emr.errors import DeserializationError
from aws_sdk_emr._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

IdcUserAssignment: TypeAlias = Literal[
    "REQUIRED",
    "OPTIONAL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REQUIRED",
        "OPTIONAL",
    )
)


def serialize_aws_json_1_1(value: IdcUserAssignment) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IdcUserAssignment:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IdcUserAssignment value: {data!r}")
    return cast(IdcUserAssignment, data)
