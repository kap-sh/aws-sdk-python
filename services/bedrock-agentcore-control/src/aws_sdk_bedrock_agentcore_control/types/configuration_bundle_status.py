"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ConfigurationBundleStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
from aws_sdk_bedrock_agentcore_control._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ConfigurationBundleStatus: TypeAlias = Literal["ACTIVE", "CREATING", "CREATE_FAILED", "UPDATING", "UPDATE_FAILED", "DELETING", "DELETE_FAILED",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ACTIVE", "CREATING", "CREATE_FAILED", "UPDATING", "UPDATE_FAILED", "DELETING", "DELETE_FAILED",))


def serialize_json(value: ConfigurationBundleStatus) -> str:
    return value


def deserialize_json(data: str) -> ConfigurationBundleStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConfigurationBundleStatus value: {data!r}")
    return cast(ConfigurationBundleStatus, data)