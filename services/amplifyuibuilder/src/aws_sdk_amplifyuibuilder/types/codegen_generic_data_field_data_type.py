"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#CodegenGenericDataFieldDataType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_amplifyuibuilder.errors import DeserializationError
from aws_sdk_amplifyuibuilder._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

CodegenGenericDataFieldDataType: TypeAlias = Literal["ID", "String", "Int", "Float", "AWSDate", "AWSTime", "AWSDateTime", "AWSTimestamp", "AWSEmail", "AWSURL", "AWSIPAddress", "Boolean", "AWSJSON", "AWSPhone", "Enum", "Model", "NonModel",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ID", "String", "Int", "Float", "AWSDate", "AWSTime", "AWSDateTime", "AWSTimestamp", "AWSEmail", "AWSURL", "AWSIPAddress", "Boolean", "AWSJSON", "AWSPhone", "Enum", "Model", "NonModel",))


def serialize_json(value: CodegenGenericDataFieldDataType) -> str:
    return value


def deserialize_json(data: str) -> CodegenGenericDataFieldDataType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CodegenGenericDataFieldDataType value: {data!r}")
    return cast(CodegenGenericDataFieldDataType, data)