"""Generated from Smithy shape ``com.amazonaws.dsql#EncryptionStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_dsql.errors import DeserializationError
from aws_sdk_dsql._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

EncryptionStatus: TypeAlias = Literal["ENABLED", "UPDATING", "KMS_KEY_INACCESSIBLE", "ENABLING",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ENABLED", "UPDATING", "KMS_KEY_INACCESSIBLE", "ENABLING",))


def serialize_json(value: EncryptionStatus) -> str:
    return value


def deserialize_json(data: str) -> EncryptionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EncryptionStatus value: {data!r}")
    return cast(EncryptionStatus, data)