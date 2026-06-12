"""Generated from Smithy shape ``com.amazonaws.neptunegraph#BlankNodeHandling``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_neptune_graph.errors import DeserializationError
from aws_sdk_neptune_graph._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

BlankNodeHandling: TypeAlias = Literal["convertToIri",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("convertToIri",))


def serialize_json(value: BlankNodeHandling) -> str:
    return value


def deserialize_json(data: str) -> BlankNodeHandling:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BlankNodeHandling value: {data!r}")
    return cast(BlankNodeHandling, data)