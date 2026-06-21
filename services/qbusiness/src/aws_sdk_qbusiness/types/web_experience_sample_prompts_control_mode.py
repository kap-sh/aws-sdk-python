"""Generated from Smithy shape ``com.amazonaws.qbusiness#WebExperienceSamplePromptsControlMode``."""

from typing import Literal, TypeAlias, cast

WebExperienceSamplePromptsControlMode: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: WebExperienceSamplePromptsControlMode) -> str:
    return value


def deserialize_json(data: str) -> WebExperienceSamplePromptsControlMode:
    return cast(WebExperienceSamplePromptsControlMode, data)
