"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#BatchEvaluationStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agentcore.errors import DeserializationError
from aws_sdk_bedrock_agentcore._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""<p>The lifecycle status of a batch evaluation job.</p>"""
BatchEvaluationStatus: TypeAlias = Literal["PENDING", "IN_PROGRESS", "COMPLETED", "COMPLETED_WITH_ERRORS", "FAILED", "STOPPING", "STOPPED", "DELETING",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("PENDING", "IN_PROGRESS", "COMPLETED", "COMPLETED_WITH_ERRORS", "FAILED", "STOPPING", "STOPPED", "DELETING",))


def serialize_json(value: BatchEvaluationStatus) -> str:
    return value


def deserialize_json(data: str) -> BatchEvaluationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BatchEvaluationStatus value: {data!r}")
    return cast(BatchEvaluationStatus, data)