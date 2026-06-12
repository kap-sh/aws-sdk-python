"""Generated from Smithy shape ``com.amazonaws.dsql#ClusterCreationTime``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_dsql.errors import DeserializationError
from aws_sdk_dsql._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""<p>The timestamp when the cluster was created.</p>"""
ClusterCreationTime: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: ClusterCreationTime) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> ClusterCreationTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)