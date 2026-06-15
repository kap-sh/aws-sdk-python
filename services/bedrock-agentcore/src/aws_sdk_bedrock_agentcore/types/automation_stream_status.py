"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#AutomationStreamStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore.errors import DeserializationError

AutomationStreamStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: AutomationStreamStatus) -> str:
    return value


def deserialize_json(data: str) -> AutomationStreamStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutomationStreamStatus value: {data!r}")
    return cast(AutomationStreamStatus, data)
