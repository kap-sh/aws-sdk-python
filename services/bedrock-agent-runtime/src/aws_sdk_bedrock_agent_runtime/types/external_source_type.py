"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ExternalSourceType``."""

from typing import Literal, TypeAlias, cast

ExternalSourceType: TypeAlias = Literal[
    "S3",
    "BYTE_CONTENT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ExternalSourceType) -> str:
    return value


def deserialize_json(data: str) -> ExternalSourceType:
    return cast(ExternalSourceType, data)
