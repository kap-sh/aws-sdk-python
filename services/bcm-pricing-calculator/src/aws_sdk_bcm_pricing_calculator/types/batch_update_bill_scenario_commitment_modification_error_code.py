"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchUpdateBillScenarioCommitmentModificationErrorCode``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bcm_pricing_calculator.errors import DeserializationError
from aws_sdk_bcm_pricing_calculator._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

BatchUpdateBillScenarioCommitmentModificationErrorCode: TypeAlias = Literal["BAD_REQUEST", "NOT_FOUND", "CONFLICT", "INTERNAL_SERVER_ERROR",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("BAD_REQUEST", "NOT_FOUND", "CONFLICT", "INTERNAL_SERVER_ERROR",))


def serialize_aws_json_1_0(value: BatchUpdateBillScenarioCommitmentModificationErrorCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BatchUpdateBillScenarioCommitmentModificationErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BatchUpdateBillScenarioCommitmentModificationErrorCode value: {data!r}")
    return cast(BatchUpdateBillScenarioCommitmentModificationErrorCode, data)