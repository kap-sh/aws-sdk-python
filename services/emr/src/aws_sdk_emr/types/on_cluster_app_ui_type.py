"""Generated from Smithy shape ``com.amazonaws.emr#OnClusterAppUIType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_emr.errors import DeserializationError
from aws_sdk_emr._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

OnClusterAppUIType: TypeAlias = Literal[
    "SparkHistoryServer",
    "YarnTimelineService",
    "TezUI",
    "ApplicationMaster",
    "JobHistoryServer",
    "ResourceManager",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SparkHistoryServer",
        "YarnTimelineService",
        "TezUI",
        "ApplicationMaster",
        "JobHistoryServer",
        "ResourceManager",
    )
)


def serialize_aws_json_1_1(value: OnClusterAppUIType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OnClusterAppUIType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OnClusterAppUIType value: {data!r}")
    return cast(OnClusterAppUIType, data)
