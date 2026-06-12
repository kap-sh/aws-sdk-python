"""Generated from Smithy shape ``com.amazonaws.connect#AiUseCase``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

AiUseCase: TypeAlias = Literal[
    "AgentAssistance",
    "SelfService",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AgentAssistance",
        "SelfService",
    )
)


def serialize_json(value: AiUseCase) -> str:
    return value


def deserialize_json(data: str) -> AiUseCase:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AiUseCase value: {data!r}")
    return cast(AiUseCase, data)
