"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GuadrailAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

GuadrailAction: TypeAlias = Literal[
    "INTERVENED",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INTERVENED",
        "NONE",
    )
)


def serialize_json(value: GuadrailAction) -> str:
    return value


def deserialize_json(data: str) -> GuadrailAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GuadrailAction value: {data!r}")
    return cast(GuadrailAction, data)
