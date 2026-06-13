"""Generated from Smithy prelude shape ``smithy.api#Blob``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, cast
from aws_sdk_storage_gateway.errors import DeserializationError
from aws_sdk_storage_gateway._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: bytes) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_1(data: str) -> bytes:
    return base64.b64decode(data)
