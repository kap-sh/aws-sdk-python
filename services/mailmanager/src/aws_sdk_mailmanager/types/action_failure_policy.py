"""Generated from Smithy shape ``com.amazonaws.mailmanager#ActionFailurePolicy``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_mailmanager.errors import DeserializationError
from aws_sdk_mailmanager._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ActionFailurePolicy: TypeAlias = Literal["CONTINUE", "DROP",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("CONTINUE", "DROP",))


def serialize_aws_json_1_0(value: ActionFailurePolicy) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ActionFailurePolicy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ActionFailurePolicy value: {data!r}")
    return cast(ActionFailurePolicy, data)