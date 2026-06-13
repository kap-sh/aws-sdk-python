"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FileUseCase``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

FileUseCase: TypeAlias = Literal[
    "CODE_INTERPRETER",
    "CHAT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CODE_INTERPRETER",
        "CHAT",
    )
)


def serialize_json(value: FileUseCase) -> str:
    return value


def deserialize_json(data: str) -> FileUseCase:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FileUseCase value: {data!r}")
    return cast(FileUseCase, data)
