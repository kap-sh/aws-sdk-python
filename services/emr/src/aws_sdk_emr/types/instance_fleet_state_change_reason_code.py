"""Generated from Smithy shape ``com.amazonaws.emr#InstanceFleetStateChangeReasonCode``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_emr.errors import DeserializationError
from aws_sdk_emr._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

InstanceFleetStateChangeReasonCode: TypeAlias = Literal[
    "INTERNAL_ERROR",
    "VALIDATION_ERROR",
    "INSTANCE_FAILURE",
    "CLUSTER_TERMINATED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INTERNAL_ERROR",
        "VALIDATION_ERROR",
        "INSTANCE_FAILURE",
        "CLUSTER_TERMINATED",
    )
)


def serialize_aws_json_1_1(value: InstanceFleetStateChangeReasonCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceFleetStateChangeReasonCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown InstanceFleetStateChangeReasonCode value: {data!r}"
        )
    return cast(InstanceFleetStateChangeReasonCode, data)
