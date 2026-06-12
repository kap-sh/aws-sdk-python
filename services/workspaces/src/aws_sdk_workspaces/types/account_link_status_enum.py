"""Generated from Smithy shape ``com.amazonaws.workspaces#AccountLinkStatusEnum``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_workspaces.errors import DeserializationError
from aws_sdk_workspaces._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

AccountLinkStatusEnum: TypeAlias = Literal[
    "LINKED",
    "LINKING_FAILED",
    "LINK_NOT_FOUND",
    "PENDING_ACCEPTANCE_BY_TARGET_ACCOUNT",
    "REJECTED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LINKED",
        "LINKING_FAILED",
        "LINK_NOT_FOUND",
        "PENDING_ACCEPTANCE_BY_TARGET_ACCOUNT",
        "REJECTED",
    )
)


def serialize_aws_json_1_1(value: AccountLinkStatusEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AccountLinkStatusEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AccountLinkStatusEnum value: {data!r}")
    return cast(AccountLinkStatusEnum, data)
