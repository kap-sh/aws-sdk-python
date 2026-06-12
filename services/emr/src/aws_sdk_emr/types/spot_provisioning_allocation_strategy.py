"""Generated from Smithy shape ``com.amazonaws.emr#SpotProvisioningAllocationStrategy``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_emr.errors import DeserializationError
from aws_sdk_emr._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

SpotProvisioningAllocationStrategy: TypeAlias = Literal[
    "capacity-optimized",
    "price-capacity-optimized",
    "lowest-price",
    "diversified",
    "capacity-optimized-prioritized",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "capacity-optimized",
        "price-capacity-optimized",
        "lowest-price",
        "diversified",
        "capacity-optimized-prioritized",
    )
)


def serialize_aws_json_1_1(value: SpotProvisioningAllocationStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SpotProvisioningAllocationStrategy:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SpotProvisioningAllocationStrategy value: {data!r}"
        )
    return cast(SpotProvisioningAllocationStrategy, data)
