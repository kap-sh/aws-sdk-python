"""Generated from Smithy shape ``com.amazonaws.emr#OnDemandProvisioningAllocationStrategy``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_emr.errors import DeserializationError
from aws_sdk_emr._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

OnDemandProvisioningAllocationStrategy: TypeAlias = Literal[
    "lowest-price",
    "prioritized",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "lowest-price",
        "prioritized",
    )
)


def serialize_aws_json_1_1(value: OnDemandProvisioningAllocationStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OnDemandProvisioningAllocationStrategy:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown OnDemandProvisioningAllocationStrategy value: {data!r}"
        )
    return cast(OnDemandProvisioningAllocationStrategy, data)
