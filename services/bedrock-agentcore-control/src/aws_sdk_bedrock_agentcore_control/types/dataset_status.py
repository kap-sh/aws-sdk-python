"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DatasetStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
from aws_sdk_bedrock_agentcore_control._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""<p> Dataset lifecycle and operation status. </p>"""
DatasetStatus: TypeAlias = Literal["CREATING", "UPDATING", "DELETING", "ACTIVE", "CREATE_FAILED", "UPDATE_FAILED", "DELETE_FAILED",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CREATING", "UPDATING", "DELETING", "ACTIVE", "CREATE_FAILED", "UPDATE_FAILED", "DELETE_FAILED",))


def serialize_json(value: DatasetStatus) -> str:
    return value


def deserialize_json(data: str) -> DatasetStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DatasetStatus value: {data!r}")
    return cast(DatasetStatus, data)