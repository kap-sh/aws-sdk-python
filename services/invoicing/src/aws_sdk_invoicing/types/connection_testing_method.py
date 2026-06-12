"""Generated from Smithy shape ``com.amazonaws.invoicing#ConnectionTestingMethod``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_invoicing.errors import DeserializationError
from aws_sdk_invoicing._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ConnectionTestingMethod: TypeAlias = Literal["PROD_ENV_DOLLAR_TEST", "TEST_ENV_REPLAY_TEST",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("PROD_ENV_DOLLAR_TEST", "TEST_ENV_REPLAY_TEST",))


def serialize_aws_json_1_0(value: ConnectionTestingMethod) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ConnectionTestingMethod:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectionTestingMethod value: {data!r}")
    return cast(ConnectionTestingMethod, data)