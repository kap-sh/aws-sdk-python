"""Generated from Smithy shape ``com.amazonaws.entityresolution#AttributeMatchingModel``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_entityresolution.errors import DeserializationError
from aws_sdk_entityresolution._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

AttributeMatchingModel: TypeAlias = Literal["ONE_TO_ONE", "MANY_TO_MANY",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ONE_TO_ONE", "MANY_TO_MANY",))


def serialize_json(value: AttributeMatchingModel) -> str:
    return value


def deserialize_json(data: str) -> AttributeMatchingModel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AttributeMatchingModel value: {data!r}")
    return cast(AttributeMatchingModel, data)