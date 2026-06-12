"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#CedarVersion``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_verifiedpermissions.errors import DeserializationError
from aws_sdk_verifiedpermissions._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

CedarVersion: TypeAlias = Literal["CEDAR_2", "CEDAR_4",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("CEDAR_2", "CEDAR_4",))


def serialize_aws_json_1_0(value: CedarVersion) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> CedarVersion:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CedarVersion value: {data!r}")
    return cast(CedarVersion, data)