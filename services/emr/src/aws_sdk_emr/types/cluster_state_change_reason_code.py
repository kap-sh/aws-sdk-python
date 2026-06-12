"""Generated from Smithy shape ``com.amazonaws.emr#ClusterStateChangeReasonCode``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_emr.errors import DeserializationError
from aws_sdk_emr._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ClusterStateChangeReasonCode: TypeAlias = Literal[
    "INTERNAL_ERROR",
    "VALIDATION_ERROR",
    "INSTANCE_FAILURE",
    "INSTANCE_FLEET_TIMEOUT",
    "BOOTSTRAP_FAILURE",
    "USER_REQUEST",
    "STEP_FAILURE",
    "ALL_STEPS_COMPLETED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INTERNAL_ERROR",
        "VALIDATION_ERROR",
        "INSTANCE_FAILURE",
        "INSTANCE_FLEET_TIMEOUT",
        "BOOTSTRAP_FAILURE",
        "USER_REQUEST",
        "STEP_FAILURE",
        "ALL_STEPS_COMPLETED",
    )
)


def serialize_aws_json_1_1(value: ClusterStateChangeReasonCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterStateChangeReasonCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ClusterStateChangeReasonCode value: {data!r}"
        )
    return cast(ClusterStateChangeReasonCode, data)
