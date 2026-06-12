"""Generated from Smithy shape ``com.amazonaws.bedrock#AcknowledgementFormDataBody``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock.errors import DeserializationError
from aws_sdk_bedrock._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

AcknowledgementFormDataBody: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: AcknowledgementFormDataBody) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> AcknowledgementFormDataBody:
    return base64.b64decode(data)
