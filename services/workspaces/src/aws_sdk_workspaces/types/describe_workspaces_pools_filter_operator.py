"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeWorkspacesPoolsFilterOperator``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_workspaces.errors import DeserializationError
from aws_sdk_workspaces._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

DescribeWorkspacesPoolsFilterOperator: TypeAlias = Literal[
    "EQUALS",
    "NOTEQUALS",
    "CONTAINS",
    "NOTCONTAINS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EQUALS",
        "NOTEQUALS",
        "CONTAINS",
        "NOTCONTAINS",
    )
)


def serialize_aws_json_1_1(value: DescribeWorkspacesPoolsFilterOperator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DescribeWorkspacesPoolsFilterOperator:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DescribeWorkspacesPoolsFilterOperator value: {data!r}"
        )
    return cast(DescribeWorkspacesPoolsFilterOperator, data)
