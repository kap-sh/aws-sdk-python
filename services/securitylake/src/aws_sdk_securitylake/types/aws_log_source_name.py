"""Generated from Smithy shape ``com.amazonaws.securitylake#AwsLogSourceName``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_securitylake.errors import DeserializationError
from aws_sdk_securitylake._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

AwsLogSourceName: TypeAlias = Literal["ROUTE53", "VPC_FLOW", "SH_FINDINGS", "CLOUD_TRAIL_MGMT", "LAMBDA_EXECUTION", "S3_DATA", "EKS_AUDIT", "WAF",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ROUTE53", "VPC_FLOW", "SH_FINDINGS", "CLOUD_TRAIL_MGMT", "LAMBDA_EXECUTION", "S3_DATA", "EKS_AUDIT", "WAF",))


def serialize_json(value: AwsLogSourceName) -> str:
    return value


def deserialize_json(data: str) -> AwsLogSourceName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AwsLogSourceName value: {data!r}")
    return cast(AwsLogSourceName, data)