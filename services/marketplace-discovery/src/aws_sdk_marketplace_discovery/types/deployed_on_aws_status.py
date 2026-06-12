"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#DeployedOnAwsStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_marketplace_discovery.errors import DeserializationError
from aws_sdk_marketplace_discovery._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

DeployedOnAwsStatus: TypeAlias = Literal["DEPLOYED", "NOT_DEPLOYED", "NOT_APPLICABLE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("DEPLOYED", "NOT_DEPLOYED", "NOT_APPLICABLE",))


def serialize_json(value: DeployedOnAwsStatus) -> str:
    return value


def deserialize_json(data: str) -> DeployedOnAwsStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeployedOnAwsStatus value: {data!r}")
    return cast(DeployedOnAwsStatus, data)