"""Generated from Smithy shape ``com.amazonaws.keyspacesstreams#Date``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_keyspacesstreams.errors import DeserializationError
from aws_sdk_keyspacesstreams._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

Date: TypeAlias = datetime.datetime


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Date) -> float:
    return value.timestamp()


def deserialize_aws_json_1_0(data: float) -> Date:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)