"""Generated from Smithy shape ``com.amazonaws.bedrockagent#SalesforceAuthType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

SalesforceAuthType: TypeAlias = Literal["OAUTH2_CLIENT_CREDENTIALS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("OAUTH2_CLIENT_CREDENTIALS",))


def serialize_json(value: SalesforceAuthType) -> str:
    return value


def deserialize_json(data: str) -> SalesforceAuthType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SalesforceAuthType value: {data!r}")
    return cast(SalesforceAuthType, data)
