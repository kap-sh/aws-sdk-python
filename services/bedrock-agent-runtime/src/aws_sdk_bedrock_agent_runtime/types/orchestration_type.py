"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#OrchestrationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

OrchestrationType: TypeAlias = Literal[
    "DEFAULT",
    "CUSTOM_ORCHESTRATION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEFAULT",
        "CUSTOM_ORCHESTRATION",
    )
)


def serialize_json(value: OrchestrationType) -> str:
    return value


def deserialize_json(data: str) -> OrchestrationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OrchestrationType value: {data!r}")
    return cast(OrchestrationType, data)
