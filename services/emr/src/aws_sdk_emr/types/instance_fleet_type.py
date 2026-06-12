"""Generated from Smithy shape ``com.amazonaws.emr#InstanceFleetType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_emr.errors import DeserializationError
from aws_sdk_emr._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

InstanceFleetType: TypeAlias = Literal[
    "MASTER",
    "CORE",
    "TASK",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MASTER",
        "CORE",
        "TASK",
    )
)


def serialize_aws_json_1_1(value: InstanceFleetType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceFleetType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InstanceFleetType value: {data!r}")
    return cast(InstanceFleetType, data)
