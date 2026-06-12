"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#AutoRecoveryEnum``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_workspaces_instances.errors import DeserializationError
from aws_sdk_workspaces_instances._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

AutoRecoveryEnum: TypeAlias = Literal["disabled", "default",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("disabled", "default",))


def serialize_aws_json_1_0(value: AutoRecoveryEnum) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AutoRecoveryEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutoRecoveryEnum value: {data!r}")
    return cast(AutoRecoveryEnum, data)