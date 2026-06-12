"""Generated from Smithy shape ``com.amazonaws.emr#ClusterState``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_emr.errors import DeserializationError
from aws_sdk_emr._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ClusterState: TypeAlias = Literal[
    "STARTING",
    "BOOTSTRAPPING",
    "RUNNING",
    "WAITING",
    "TERMINATING",
    "TERMINATED",
    "TERMINATED_WITH_ERRORS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STARTING",
        "BOOTSTRAPPING",
        "RUNNING",
        "WAITING",
        "TERMINATING",
        "TERMINATED",
        "TERMINATED_WITH_ERRORS",
    )
)


def serialize_aws_json_1_1(value: ClusterState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ClusterState value: {data!r}")
    return cast(ClusterState, data)
