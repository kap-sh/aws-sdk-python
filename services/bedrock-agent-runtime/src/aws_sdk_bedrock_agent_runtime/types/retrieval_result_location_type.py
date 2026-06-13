"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrievalResultLocationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "S3",
        "WEB",
        "CONFLUENCE",
        "SALESFORCE",
        "SHAREPOINT",
        "CUSTOM",
        "KENDRA",
        "SQL",
    )
)


def serialize_json(value: RetrievalResultLocationType) -> str:
    return value


def deserialize_json(data: str) -> RetrievalResultLocationType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RetrievalResultLocationType value: {data!r}"
        )
    return cast(RetrievalResultLocationType, data)
