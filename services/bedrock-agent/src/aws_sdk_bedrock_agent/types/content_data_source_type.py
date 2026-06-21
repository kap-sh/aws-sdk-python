"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ContentDataSourceType``."""

from typing import Literal, TypeAlias, cast

ContentDataSourceType: TypeAlias = Literal[
    "CUSTOM",
    "S3",
]


# --- restJson1 ser/de ---
def serialize_json(value: ContentDataSourceType) -> str:
    return value


def deserialize_json(data: str) -> ContentDataSourceType:
    return cast(ContentDataSourceType, data)
