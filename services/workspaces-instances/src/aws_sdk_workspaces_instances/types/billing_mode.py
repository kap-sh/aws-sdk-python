"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#BillingMode``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_workspaces_instances.errors import DeserializationError
from aws_sdk_workspaces_instances._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

BillingMode: TypeAlias = Literal["MONTHLY", "HOURLY",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("MONTHLY", "HOURLY",))


def serialize_aws_json_1_0(value: BillingMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BillingMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BillingMode value: {data!r}")
    return cast(BillingMode, data)