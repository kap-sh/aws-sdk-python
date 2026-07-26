"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrievalResultLocationType``."""

from typing import Literal, TypeAlias, cast

RetrievalResultLocationType: TypeAlias = Literal[
    "S3",
    "WEB",
    "CONFLUENCE",
    "SALESFORCE",
    "SHAREPOINT",
    "CUSTOM",
    "KENDRA",
    "SQL",
]


# --- restJson1 ser/de ---
def serialize_json(value: RetrievalResultLocationType) -> str:
    return value


def deserialize_json(data: str) -> RetrievalResultLocationType:
    return cast(RetrievalResultLocationType, data)
