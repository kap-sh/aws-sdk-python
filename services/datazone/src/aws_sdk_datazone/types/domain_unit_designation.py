"""Generated from Smithy shape ``com.amazonaws.datazone#DomainUnitDesignation``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

DomainUnitDesignation: TypeAlias = Literal["OWNER",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("OWNER",))


def serialize_json(value: DomainUnitDesignation) -> str:
    return value


def deserialize_json(data: str) -> DomainUnitDesignation:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DomainUnitDesignation value: {data!r}")
    return cast(DomainUnitDesignation, data)
