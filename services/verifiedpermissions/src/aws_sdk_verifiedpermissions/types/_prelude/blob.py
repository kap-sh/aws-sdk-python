"""Generated from Smithy prelude shape ``smithy.api#Blob``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, cast
from aws_sdk_verifiedpermissions.errors import DeserializationError
from aws_sdk_verifiedpermissions._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: bytes) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_0(data: str) -> bytes:
    return base64.b64decode(data)