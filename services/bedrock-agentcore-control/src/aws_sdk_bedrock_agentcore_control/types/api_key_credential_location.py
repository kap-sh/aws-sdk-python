"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ApiKeyCredentialLocation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

ApiKeyCredentialLocation: TypeAlias = Literal[
    "HEADER",
    "QUERY_PARAMETER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HEADER",
        "QUERY_PARAMETER",
    )
)


def serialize_json(value: ApiKeyCredentialLocation) -> str:
    return value


def deserialize_json(data: str) -> ApiKeyCredentialLocation:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ApiKeyCredentialLocation value: {data!r}")
    return cast(ApiKeyCredentialLocation, data)
