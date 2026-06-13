"""Generated from Smithy shape ``com.amazonaws.datazone#SearchOutputAdditionalAttribute``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

SearchOutputAdditionalAttribute: TypeAlias = Literal[
    "FORMS",
    "TIME_SERIES_DATA_POINT_FORMS",
    "TEXT_MATCH_RATIONALE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FORMS",
        "TIME_SERIES_DATA_POINT_FORMS",
        "TEXT_MATCH_RATIONALE",
    )
)


def serialize_json(value: SearchOutputAdditionalAttribute) -> str:
    return value


def deserialize_json(data: str) -> SearchOutputAdditionalAttribute:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SearchOutputAdditionalAttribute value: {data!r}"
        )
    return cast(SearchOutputAdditionalAttribute, data)
