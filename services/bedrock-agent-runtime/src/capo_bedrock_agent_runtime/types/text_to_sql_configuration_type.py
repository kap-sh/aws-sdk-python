"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#TextToSqlConfigurationType``."""

from typing import Literal, TypeAlias, cast

TextToSqlConfigurationType: TypeAlias = Literal["KNOWLEDGE_BASE",]


# --- restJson1 ser/de ---
def serialize_json(value: TextToSqlConfigurationType) -> str:
    return value


def deserialize_json(data: str) -> TextToSqlConfigurationType:
    return cast(TextToSqlConfigurationType, data)
