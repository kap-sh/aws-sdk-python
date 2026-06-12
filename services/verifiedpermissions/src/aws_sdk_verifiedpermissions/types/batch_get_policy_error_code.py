"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#BatchGetPolicyErrorCode``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_verifiedpermissions.errors import DeserializationError
from aws_sdk_verifiedpermissions._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

BatchGetPolicyErrorCode: TypeAlias = Literal["POLICY_STORE_NOT_FOUND", "POLICY_NOT_FOUND", "POLICY_STORE_ALIAS_NOT_FOUND",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("POLICY_STORE_NOT_FOUND", "POLICY_NOT_FOUND", "POLICY_STORE_ALIAS_NOT_FOUND",))


def serialize_aws_json_1_0(value: BatchGetPolicyErrorCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BatchGetPolicyErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BatchGetPolicyErrorCode value: {data!r}")
    return cast(BatchGetPolicyErrorCode, data)