"""Generated from Smithy shape ``com.amazonaws.backup#BackupJobStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_backup.errors import DeserializationError
from aws_sdk_backup._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

BackupJobStatus: TypeAlias = Literal["CREATED", "PENDING", "RUNNING", "ABORTING", "ABORTED", "COMPLETED", "FAILED", "EXPIRED", "PARTIAL", "AGGREGATE_ALL", "ANY",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CREATED", "PENDING", "RUNNING", "ABORTING", "ABORTED", "COMPLETED", "FAILED", "EXPIRED", "PARTIAL", "AGGREGATE_ALL", "ANY",))


def serialize_json(value: BackupJobStatus) -> str:
    return value


def deserialize_json(data: str) -> BackupJobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BackupJobStatus value: {data!r}")
    return cast(BackupJobStatus, data)