"""Generated from Smithy prelude shape ``smithy.api#Timestamp``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, cast
from aws_sdk_cloudwatch_logs.errors import DeserializationError
from aws_sdk_cloudwatch_logs._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: datetime.datetime) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> datetime.datetime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
