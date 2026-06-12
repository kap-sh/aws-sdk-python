"""Generated from Smithy shape ``com.amazonaws.backup#BackupJobState``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_backup.errors import DeserializationError
from aws_sdk_backup._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

BackupJobState: TypeAlias = Literal["CREATED", "PENDING", "RUNNING", "ABORTING", "ABORTED", "COMPLETED", "FAILED", "EXPIRED", "PARTIAL",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CREATED", "PENDING", "RUNNING", "ABORTING", "ABORTED", "COMPLETED", "FAILED", "EXPIRED", "PARTIAL",))


def serialize_json(value: BackupJobState) -> str:
    return value


def deserialize_json(data: str) -> BackupJobState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BackupJobState value: {data!r}")
    return cast(BackupJobState, data)