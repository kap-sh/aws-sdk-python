"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#InstanceConfigurationTenancyEnum``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_workspaces_instances.errors import DeserializationError
from aws_sdk_workspaces_instances._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

InstanceConfigurationTenancyEnum: TypeAlias = Literal["SHARED", "DEDICATED",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("SHARED", "DEDICATED",))


def serialize_aws_json_1_0(value: InstanceConfigurationTenancyEnum) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> InstanceConfigurationTenancyEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InstanceConfigurationTenancyEnum value: {data!r}")
    return cast(InstanceConfigurationTenancyEnum, data)