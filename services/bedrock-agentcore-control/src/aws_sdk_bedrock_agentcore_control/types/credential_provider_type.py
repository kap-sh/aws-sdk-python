"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CredentialProviderType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
from aws_sdk_bedrock_agentcore_control._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

CredentialProviderType: TypeAlias = Literal["GATEWAY_IAM_ROLE", "OAUTH", "API_KEY", "CALLER_IAM_CREDENTIALS", "JWT_PASSTHROUGH",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("GATEWAY_IAM_ROLE", "OAUTH", "API_KEY", "CALLER_IAM_CREDENTIALS", "JWT_PASSTHROUGH",))


def serialize_json(value: CredentialProviderType) -> str:
    return value


def deserialize_json(data: str) -> CredentialProviderType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CredentialProviderType value: {data!r}")
    return cast(CredentialProviderType, data)