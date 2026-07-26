"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessOpenAiApiFormat``."""

from typing import Literal, TypeAlias, cast

HarnessOpenAiApiFormat: TypeAlias = Literal[
    "chat_completions",
    "responses",
]


# --- restJson1 ser/de ---
def serialize_json(value: HarnessOpenAiApiFormat) -> str:
    return value


def deserialize_json(data: str) -> HarnessOpenAiApiFormat:
    return cast(HarnessOpenAiApiFormat, data)
