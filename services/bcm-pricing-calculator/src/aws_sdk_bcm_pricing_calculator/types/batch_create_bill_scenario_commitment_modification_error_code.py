"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchCreateBillScenarioCommitmentModificationErrorCode``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bcm_pricing_calculator.errors import DeserializationError
from aws_sdk_bcm_pricing_calculator._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

BatchCreateBillScenarioCommitmentModificationErrorCode: TypeAlias = Literal["CONFLICT", "INTERNAL_SERVER_ERROR", "INVALID_ACCOUNT",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("CONFLICT", "INTERNAL_SERVER_ERROR", "INVALID_ACCOUNT",))


def serialize_aws_json_1_0(value: BatchCreateBillScenarioCommitmentModificationErrorCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BatchCreateBillScenarioCommitmentModificationErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BatchCreateBillScenarioCommitmentModificationErrorCode value: {data!r}")
    return cast(BatchCreateBillScenarioCommitmentModificationErrorCode, data)