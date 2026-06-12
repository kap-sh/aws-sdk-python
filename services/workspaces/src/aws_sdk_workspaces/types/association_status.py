"""Generated from Smithy shape ``com.amazonaws.workspaces#AssociationStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_workspaces.errors import DeserializationError
from aws_sdk_workspaces._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

AssociationStatus: TypeAlias = Literal[
    "NOT_ASSOCIATED",
    "ASSOCIATED_WITH_OWNER_ACCOUNT",
    "ASSOCIATED_WITH_SHARED_ACCOUNT",
    "PENDING_ASSOCIATION",
    "PENDING_DISASSOCIATION",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NOT_ASSOCIATED",
        "ASSOCIATED_WITH_OWNER_ACCOUNT",
        "ASSOCIATED_WITH_SHARED_ACCOUNT",
        "PENDING_ASSOCIATION",
        "PENDING_DISASSOCIATION",
    )
)


def serialize_aws_json_1_1(value: AssociationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AssociationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AssociationStatus value: {data!r}")
    return cast(AssociationStatus, data)
