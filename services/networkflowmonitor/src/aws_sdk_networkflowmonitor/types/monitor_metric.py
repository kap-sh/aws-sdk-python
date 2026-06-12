"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#MonitorMetric``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_networkflowmonitor.errors import DeserializationError
from aws_sdk_networkflowmonitor._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

MonitorMetric: TypeAlias = Literal["ROUND_TRIP_TIME", "TIMEOUTS", "RETRANSMISSIONS", "DATA_TRANSFERRED",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ROUND_TRIP_TIME", "TIMEOUTS", "RETRANSMISSIONS", "DATA_TRANSFERRED",))


def serialize_json(value: MonitorMetric) -> str:
    return value


def deserialize_json(data: str) -> MonitorMetric:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MonitorMetric value: {data!r}")
    return cast(MonitorMetric, data)