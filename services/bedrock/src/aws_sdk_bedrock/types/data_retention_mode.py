"""Generated from Smithy shape ``com.amazonaws.bedrock#DataRetentionMode``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock.errors import DeserializationError
from aws_sdk_bedrock._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""<p>The data retention mode for the account. Valid values are:</p> <ul> <li> <p> <code>default</code> – The standard data handling for the model applies.</p> </li> <li> <p> <code>none</code> – Zero data retention.</p> </li> <li> <p> <code>provider_data_share</code> – Data may be shared with the model provider.</p> </li> <li> <p> <code>inherit</code> – No data retention mode is set at this scope.</p> </li> </ul>"""
DataRetentionMode: TypeAlias = Literal[
    "default",
    "none",
    "provider_data_share",
    "inherit",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "default",
        "none",
        "provider_data_share",
        "inherit",
    )
)


def serialize_json(value: DataRetentionMode) -> str:
    return value


def deserialize_json(data: str) -> DataRetentionMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataRetentionMode value: {data!r}")
    return cast(DataRetentionMode, data)
