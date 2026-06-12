"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#AliasState``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_verifiedpermissions.errors import DeserializationError
from aws_sdk_verifiedpermissions._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

AliasState: TypeAlias = Literal["Active", "PendingDeletion",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("Active", "PendingDeletion",))


def serialize_aws_json_1_0(value: AliasState) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AliasState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AliasState value: {data!r}")
    return cast(AliasState, data)