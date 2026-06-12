"""Generated from Smithy shape ``com.amazonaws.bedrockagent#SharePointAuthType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

SharePointAuthType: TypeAlias = Literal[
    "OAUTH2_CLIENT_CREDENTIALS",
    "OAUTH2_SHAREPOINT_APP_ONLY_CLIENT_CREDENTIALS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OAUTH2_CLIENT_CREDENTIALS",
        "OAUTH2_SHAREPOINT_APP_ONLY_CLIENT_CREDENTIALS",
    )
)


def serialize_json(value: SharePointAuthType) -> str:
    return value


def deserialize_json(data: str) -> SharePointAuthType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SharePointAuthType value: {data!r}")
    return cast(SharePointAuthType, data)
