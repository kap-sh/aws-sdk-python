"""Generated from Smithy shape ``com.amazonaws.dsql#EncryptionType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_dsql.errors import DeserializationError
from aws_sdk_dsql._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

EncryptionType: TypeAlias = Literal["AWS_OWNED_KMS_KEY", "CUSTOMER_MANAGED_KMS_KEY",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("AWS_OWNED_KMS_KEY", "CUSTOMER_MANAGED_KMS_KEY",))


def serialize_json(value: EncryptionType) -> str:
    return value


def deserialize_json(data: str) -> EncryptionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EncryptionType value: {data!r}")
    return cast(EncryptionType, data)