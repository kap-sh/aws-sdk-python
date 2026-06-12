"""Generated from Smithy shape ``com.amazonaws.inspector2#AssociationResultStatusCode``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_inspector2.errors import DeserializationError
from aws_sdk_inspector2._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

AssociationResultStatusCode: TypeAlias = Literal["INTERNAL_ERROR", "ACCESS_DENIED", "SCAN_CONFIGURATION_NOT_FOUND", "INVALID_INPUT", "RESOURCE_NOT_FOUND", "QUOTA_EXCEEDED",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("INTERNAL_ERROR", "ACCESS_DENIED", "SCAN_CONFIGURATION_NOT_FOUND", "INVALID_INPUT", "RESOURCE_NOT_FOUND", "QUOTA_EXCEEDED",))


def serialize_json(value: AssociationResultStatusCode) -> str:
    return value


def deserialize_json(data: str) -> AssociationResultStatusCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AssociationResultStatusCode value: {data!r}")
    return cast(AssociationResultStatusCode, data)