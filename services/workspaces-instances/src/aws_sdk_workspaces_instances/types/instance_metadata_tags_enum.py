"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#InstanceMetadataTagsEnum``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_workspaces_instances.errors import DeserializationError
from aws_sdk_workspaces_instances._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

InstanceMetadataTagsEnum: TypeAlias = Literal["enabled", "disabled",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("enabled", "disabled",))


def serialize_aws_json_1_0(value: InstanceMetadataTagsEnum) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> InstanceMetadataTagsEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InstanceMetadataTagsEnum value: {data!r}")
    return cast(InstanceMetadataTagsEnum, data)