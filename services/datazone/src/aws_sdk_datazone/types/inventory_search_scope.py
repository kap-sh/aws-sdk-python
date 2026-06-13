"""Generated from Smithy shape ``com.amazonaws.datazone#InventorySearchScope``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

InventorySearchScope: TypeAlias = Literal[
    "ASSET",
    "GLOSSARY",
    "GLOSSARY_TERM",
    "DATA_PRODUCT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASSET",
        "GLOSSARY",
        "GLOSSARY_TERM",
        "DATA_PRODUCT",
    )
)


def serialize_json(value: InventorySearchScope) -> str:
    return value


def deserialize_json(data: str) -> InventorySearchScope:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InventorySearchScope value: {data!r}")
    return cast(InventorySearchScope, data)
