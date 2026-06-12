"""Generated from Smithy shape ``com.amazonaws.invoicing#BuyerDomain``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_invoicing.errors import DeserializationError
from aws_sdk_invoicing._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

BuyerDomain: TypeAlias = Literal["NetworkID",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("NetworkID",))


def serialize_aws_json_1_0(value: BuyerDomain) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BuyerDomain:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BuyerDomain value: {data!r}")
    return cast(BuyerDomain, data)