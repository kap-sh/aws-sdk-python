"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#Distribution``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_cloudwatch_logs.errors import DeserializationError
from aws_sdk_cloudwatch_logs._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""<p>The method used to distribute log data to the destination, which can be either random or grouped by log stream.</p>"""
Distribution: TypeAlias = Literal[
    "Random",
    "ByLogStream",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Random",
        "ByLogStream",
    )
)


def serialize_aws_json_1_1(value: Distribution) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Distribution:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Distribution value: {data!r}")
    return cast(Distribution, data)
