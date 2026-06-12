"""Generated from Smithy shape ``com.amazonaws.workspaces#CertificateBasedAuthStatusEnum``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_workspaces.errors import DeserializationError
from aws_sdk_workspaces._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

CertificateBasedAuthStatusEnum: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "ENABLED",
    )
)


def serialize_aws_json_1_1(value: CertificateBasedAuthStatusEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CertificateBasedAuthStatusEnum:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CertificateBasedAuthStatusEnum value: {data!r}"
        )
    return cast(CertificateBasedAuthStatusEnum, data)
