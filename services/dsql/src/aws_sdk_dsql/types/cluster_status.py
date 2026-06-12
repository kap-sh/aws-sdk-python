"""Generated from Smithy shape ``com.amazonaws.dsql#ClusterStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_dsql.errors import DeserializationError
from aws_sdk_dsql._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""<p>The current status of a cluster.</p>"""
ClusterStatus: TypeAlias = Literal["CREATING", "ACTIVE", "IDLE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "PENDING_SETUP", "PENDING_DELETE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CREATING", "ACTIVE", "IDLE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "PENDING_SETUP", "PENDING_DELETE",))


def serialize_json(value: ClusterStatus) -> str:
    return value


def deserialize_json(data: str) -> ClusterStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ClusterStatus value: {data!r}")
    return cast(ClusterStatus, data)