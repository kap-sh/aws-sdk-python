"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#MarketTypeEnum``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_workspaces_instances.errors import DeserializationError
from aws_sdk_workspaces_instances._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

MarketTypeEnum: TypeAlias = Literal["spot", "capacity-block",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("spot", "capacity-block",))


def serialize_aws_json_1_0(value: MarketTypeEnum) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> MarketTypeEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MarketTypeEnum value: {data!r}")
    return cast(MarketTypeEnum, data)