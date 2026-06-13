"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ClientAuthenticationMethodType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
from aws_sdk_bedrock_agentcore_control._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ClientAuthenticationMethodType: TypeAlias = Literal["CLIENT_SECRET_BASIC", "CLIENT_SECRET_POST", "AWS_IAM_ID_TOKEN_JWT",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CLIENT_SECRET_BASIC", "CLIENT_SECRET_POST", "AWS_IAM_ID_TOKEN_JWT",))


def serialize_json(value: ClientAuthenticationMethodType) -> str:
    return value


def deserialize_json(data: str) -> ClientAuthenticationMethodType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ClientAuthenticationMethodType value: {data!r}")
    return cast(ClientAuthenticationMethodType, data)