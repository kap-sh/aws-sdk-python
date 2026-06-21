"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessBedrockApiFormat``."""

from typing import Literal, TypeAlias, cast

HarnessBedrockApiFormat: TypeAlias = Literal[
    "converse_stream",
    "responses",
    "chat_completions",
]


# --- restJson1 ser/de ---
def serialize_json(value: HarnessBedrockApiFormat) -> str:
    return value


def deserialize_json(data: str) -> HarnessBedrockApiFormat:
    return cast(HarnessBedrockApiFormat, data)
