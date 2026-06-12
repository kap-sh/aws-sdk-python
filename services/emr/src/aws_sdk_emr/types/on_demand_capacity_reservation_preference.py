"""Generated from Smithy shape ``com.amazonaws.emr#OnDemandCapacityReservationPreference``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_emr.errors import DeserializationError
from aws_sdk_emr._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

OnDemandCapacityReservationPreference: TypeAlias = Literal[
    "open",
    "none",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "open",
        "none",
    )
)


def serialize_aws_json_1_1(value: OnDemandCapacityReservationPreference) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OnDemandCapacityReservationPreference:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown OnDemandCapacityReservationPreference value: {data!r}"
        )
    return cast(OnDemandCapacityReservationPreference, data)
