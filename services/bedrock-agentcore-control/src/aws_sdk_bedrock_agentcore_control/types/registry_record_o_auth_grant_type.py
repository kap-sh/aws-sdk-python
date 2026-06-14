"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#RegistryRecordOAuthGrantType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

RegistryRecordOAuthGrantType: TypeAlias = Literal["CLIENT_CREDENTIALS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CLIENT_CREDENTIALS",))


def serialize_json(value: RegistryRecordOAuthGrantType) -> str:
    return value


def deserialize_json(data: str) -> RegistryRecordOAuthGrantType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RegistryRecordOAuthGrantType value: {data!r}"
        )
    return cast(RegistryRecordOAuthGrantType, data)
