"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FileUseCase``."""

from typing import Literal, TypeAlias, cast

FileUseCase: TypeAlias = Literal[
    "CODE_INTERPRETER",
    "CHAT",
]


# --- restJson1 ser/de ---
def serialize_json(value: FileUseCase) -> str:
    return value


def deserialize_json(data: str) -> FileUseCase:
    return cast(FileUseCase, data)
