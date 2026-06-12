"""Generated from Smithy shape ``com.amazonaws.s3vectors#DistanceMetric``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_s3vectors.errors import DeserializationError
from aws_sdk_s3vectors._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

DistanceMetric: TypeAlias = Literal["euclidean", "cosine",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("euclidean", "cosine",))


def serialize_json(value: DistanceMetric) -> str:
    return value


def deserialize_json(data: str) -> DistanceMetric:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DistanceMetric value: {data!r}")
    return cast(DistanceMetric, data)