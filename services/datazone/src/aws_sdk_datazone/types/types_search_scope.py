"""Generated from Smithy shape ``com.amazonaws.datazone#TypesSearchScope``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

TypesSearchScope: TypeAlias = Literal[
    "ASSET_TYPE",
    "FORM_TYPE",
    "LINEAGE_NODE_TYPE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASSET_TYPE",
        "FORM_TYPE",
        "LINEAGE_NODE_TYPE",
    )
)


def serialize_json(value: TypesSearchScope) -> str:
    return value


def deserialize_json(data: str) -> TypesSearchScope:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TypesSearchScope value: {data!r}")
    return cast(TypesSearchScope, data)
