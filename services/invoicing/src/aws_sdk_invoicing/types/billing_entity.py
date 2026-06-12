"""Generated from Smithy shape ``com.amazonaws.invoicing#BillingEntity``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_invoicing.errors import DeserializationError
from aws_sdk_invoicing._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

BillingEntity: TypeAlias = Literal["AWS", "AWS_MARKETPLACE",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("AWS", "AWS_MARKETPLACE",))


def serialize_aws_json_1_0(value: BillingEntity) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BillingEntity:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BillingEntity value: {data!r}")
    return cast(BillingEntity, data)