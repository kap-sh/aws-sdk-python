"""Generated from Smithy prelude shape ``smithy.api#Blob``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, cast
from aws_sdk_cloudsearch_domain.errors import DeserializationError
from aws_sdk_cloudsearch_domain._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http


# --- restJson1 ser/de ---
def serialize_json(value: bytes) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> bytes:
    return base64.b64decode(data)
