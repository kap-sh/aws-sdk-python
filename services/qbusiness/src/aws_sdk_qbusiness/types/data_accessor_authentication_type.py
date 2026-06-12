"""Generated from Smithy shape ``com.amazonaws.qbusiness#DataAccessorAuthenticationType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_qbusiness.errors import DeserializationError
from aws_sdk_qbusiness._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""<p>The type of authentication mechanism used by the data accessor.</p>"""
DataAccessorAuthenticationType: TypeAlias = Literal["AWS_IAM_IDC_TTI", "AWS_IAM_IDC_AUTH_CODE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("AWS_IAM_IDC_TTI", "AWS_IAM_IDC_AUTH_CODE",))


def serialize_json(value: DataAccessorAuthenticationType) -> str:
    return value


def deserialize_json(data: str) -> DataAccessorAuthenticationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataAccessorAuthenticationType value: {data!r}")
    return cast(DataAccessorAuthenticationType, data)