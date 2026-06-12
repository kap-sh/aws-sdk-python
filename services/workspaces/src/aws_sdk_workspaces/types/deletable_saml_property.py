"""Generated from Smithy shape ``com.amazonaws.workspaces#DeletableSamlProperty``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_workspaces.errors import DeserializationError
from aws_sdk_workspaces._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

DeletableSamlProperty: TypeAlias = Literal[
    "SAML_PROPERTIES_USER_ACCESS_URL",
    "SAML_PROPERTIES_RELAY_STATE_PARAMETER_NAME",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SAML_PROPERTIES_USER_ACCESS_URL",
        "SAML_PROPERTIES_RELAY_STATE_PARAMETER_NAME",
    )
)


def serialize_aws_json_1_1(value: DeletableSamlProperty) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeletableSamlProperty:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeletableSamlProperty value: {data!r}")
    return cast(DeletableSamlProperty, data)
