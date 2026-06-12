"""Generated from Smithy shape ``com.amazonaws.storagegateway#SMBSecurityStrategy``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_storage_gateway.errors import DeserializationError
from aws_sdk_storage_gateway._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

SMBSecurityStrategy: TypeAlias = Literal[
    "ClientSpecified",
    "MandatorySigning",
    "MandatoryEncryption",
    "MandatoryEncryptionNoAes128",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ClientSpecified",
        "MandatorySigning",
        "MandatoryEncryption",
        "MandatoryEncryptionNoAes128",
    )
)


def serialize_aws_json_1_1(value: SMBSecurityStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SMBSecurityStrategy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SMBSecurityStrategy value: {data!r}")
    return cast(SMBSecurityStrategy, data)
