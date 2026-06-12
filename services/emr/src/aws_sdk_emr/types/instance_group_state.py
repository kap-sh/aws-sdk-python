"""Generated from Smithy shape ``com.amazonaws.emr#InstanceGroupState``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_emr.errors import DeserializationError
from aws_sdk_emr._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

InstanceGroupState: TypeAlias = Literal[
    "PROVISIONING",
    "BOOTSTRAPPING",
    "RUNNING",
    "RECONFIGURING",
    "RESIZING",
    "SUSPENDED",
    "TERMINATING",
    "TERMINATED",
    "ARRESTED",
    "SHUTTING_DOWN",
    "ENDED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PROVISIONING",
        "BOOTSTRAPPING",
        "RUNNING",
        "RECONFIGURING",
        "RESIZING",
        "SUSPENDED",
        "TERMINATING",
        "TERMINATED",
        "ARRESTED",
        "SHUTTING_DOWN",
        "ENDED",
    )
)


def serialize_aws_json_1_1(value: InstanceGroupState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceGroupState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InstanceGroupState value: {data!r}")
    return cast(InstanceGroupState, data)
