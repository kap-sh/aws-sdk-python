"""Generated from Smithy shape ``com.amazonaws.workspaces#UserIdentityType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_workspaces.errors import DeserializationError
from aws_sdk_workspaces._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

UserIdentityType: TypeAlias = Literal[
    "CUSTOMER_MANAGED",
    "AWS_DIRECTORY_SERVICE",
    "AWS_IAM_IDENTITY_CENTER",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CUSTOMER_MANAGED",
        "AWS_DIRECTORY_SERVICE",
        "AWS_IAM_IDENTITY_CENTER",
    )
)


def serialize_aws_json_1_1(value: UserIdentityType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UserIdentityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UserIdentityType value: {data!r}")
    return cast(UserIdentityType, data)
