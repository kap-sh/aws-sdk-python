"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessToolUseStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore.errors import DeserializationError

HarnessToolUseStatus: TypeAlias = Literal[
    "success",
    "error",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "success",
        "error",
    )
)


def serialize_json(value: HarnessToolUseStatus) -> str:
    return value


def deserialize_json(data: str) -> HarnessToolUseStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HarnessToolUseStatus value: {data!r}")
    return cast(HarnessToolUseStatus, data)
