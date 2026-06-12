"""Generated from Smithy shape ``com.amazonaws.cloudsearchdomain#QueryParser``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_cloudsearch_domain.errors import DeserializationError
from aws_sdk_cloudsearch_domain._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

QueryParser: TypeAlias = Literal[
    "simple",
    "structured",
    "lucene",
    "dismax",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "simple",
        "structured",
        "lucene",
        "dismax",
    )
)


def serialize_json(value: QueryParser) -> str:
    return value


def deserialize_json(data: str) -> QueryParser:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QueryParser value: {data!r}")
    return cast(QueryParser, data)
