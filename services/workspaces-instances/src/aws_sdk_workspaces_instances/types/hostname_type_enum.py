"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#HostnameTypeEnum``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_workspaces_instances.errors import DeserializationError
from aws_sdk_workspaces_instances._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

HostnameTypeEnum: TypeAlias = Literal["ip-name", "resource-name",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("ip-name", "resource-name",))


def serialize_aws_json_1_0(value: HostnameTypeEnum) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> HostnameTypeEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HostnameTypeEnum value: {data!r}")
    return cast(HostnameTypeEnum, data)