"""Generated from Smithy shape ``com.amazonaws.pcs#AccountingMode``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_pcs.errors import DeserializationError
from aws_sdk_pcs._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

AccountingMode: TypeAlias = Literal["STANDARD", "NONE",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("STANDARD", "NONE",))


def serialize_aws_json_1_0(value: AccountingMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AccountingMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AccountingMode value: {data!r}")
    return cast(AccountingMode, data)