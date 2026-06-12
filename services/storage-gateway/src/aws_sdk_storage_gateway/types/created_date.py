"""Generated from Smithy shape ``com.amazonaws.storagegateway#CreatedDate``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_storage_gateway.errors import DeserializationError
from aws_sdk_storage_gateway._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

CreatedDate: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatedDate) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> CreatedDate:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
