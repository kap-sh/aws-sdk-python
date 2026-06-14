"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CodeInterpreterSessionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore.errors import DeserializationError

CodeInterpreterSessionStatus: TypeAlias = Literal[
    "READY",
    "TERMINATED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "READY",
        "TERMINATED",
    )
)


def serialize_json(value: CodeInterpreterSessionStatus) -> str:
    return value


def deserialize_json(data: str) -> CodeInterpreterSessionStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CodeInterpreterSessionStatus value: {data!r}"
        )
    return cast(CodeInterpreterSessionStatus, data)
