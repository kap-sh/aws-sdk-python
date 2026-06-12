"""Generated from Smithy shape ``com.amazonaws.emr#ActionOnFailure``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_emr.errors import DeserializationError
from aws_sdk_emr._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ActionOnFailure: TypeAlias = Literal[
    "TERMINATE_JOB_FLOW",
    "TERMINATE_CLUSTER",
    "CANCEL_AND_WAIT",
    "CONTINUE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TERMINATE_JOB_FLOW",
        "TERMINATE_CLUSTER",
        "CANCEL_AND_WAIT",
        "CONTINUE",
    )
)


def serialize_aws_json_1_1(value: ActionOnFailure) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ActionOnFailure:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ActionOnFailure value: {data!r}")
    return cast(ActionOnFailure, data)
