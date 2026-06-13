"""Generated from Smithy shape ``com.amazonaws.datazone#RuleAction``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

RuleAction: TypeAlias = Literal[
    "CREATE_LISTING_CHANGE_SET",
    "CREATE_SUBSCRIPTION_REQUEST",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATE_LISTING_CHANGE_SET",
        "CREATE_SUBSCRIPTION_REQUEST",
    )
)


def serialize_json(value: RuleAction) -> str:
    return value


def deserialize_json(data: str) -> RuleAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RuleAction value: {data!r}")
    return cast(RuleAction, data)
