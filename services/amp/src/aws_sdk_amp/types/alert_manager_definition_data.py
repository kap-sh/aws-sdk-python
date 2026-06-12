"""Generated from Smithy shape ``com.amazonaws.amp#AlertManagerDefinitionData``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_amp.errors import DeserializationError
from aws_sdk_amp._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""<p>The base-64 encoded blob that is alert manager definition.</p> <p>For details about the alert manager definition, see <a href=\"https://docs.aws.amazon.com/prometheus/latest/APIReference/yaml-AlertManagerDefinitionData.html\">AlertManagedDefinitionData</a>.</p>"""
AlertManagerDefinitionData: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: AlertManagerDefinitionData) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> AlertManagerDefinitionData:
    return base64.b64decode(data)