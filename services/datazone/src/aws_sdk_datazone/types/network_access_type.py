"""Generated from Smithy shape ``com.amazonaws.datazone#NetworkAccessType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""<p>The network access type for a notebook run in Amazon SageMaker Unified Studio.</p>"""
NetworkAccessType: TypeAlias = Literal[
    "PUBLIC_INTERNET_ONLY",
    "VPC_ONLY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PUBLIC_INTERNET_ONLY",
        "VPC_ONLY",
    )
)


def serialize_json(value: NetworkAccessType) -> str:
    return value


def deserialize_json(data: str) -> NetworkAccessType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NetworkAccessType value: {data!r}")
    return cast(NetworkAccessType, data)
