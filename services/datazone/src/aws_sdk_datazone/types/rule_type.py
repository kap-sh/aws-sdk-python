"""Generated from Smithy shape ``com.amazonaws.datazone#RuleType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

RuleType: TypeAlias = Literal[
    "METADATA_FORM_ENFORCEMENT",
    "GLOSSARY_TERM_ENFORCEMENT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "METADATA_FORM_ENFORCEMENT",
        "GLOSSARY_TERM_ENFORCEMENT",
    )
)


def serialize_json(value: RuleType) -> str:
    return value


def deserialize_json(data: str) -> RuleType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RuleType value: {data!r}")
    return cast(RuleType, data)
