"""Generated from Smithy shape ``com.amazonaws.bedrockagent#KnowledgeBaseStorageType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

KnowledgeBaseStorageType: TypeAlias = Literal[
    "OPENSEARCH_SERVERLESS",
    "PINECONE",
    "REDIS_ENTERPRISE_CLOUD",
    "RDS",
    "MONGO_DB_ATLAS",
    "NEPTUNE_ANALYTICS",
    "OPENSEARCH_MANAGED_CLUSTER",
    "S3_VECTORS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OPENSEARCH_SERVERLESS",
        "PINECONE",
        "REDIS_ENTERPRISE_CLOUD",
        "RDS",
        "MONGO_DB_ATLAS",
        "NEPTUNE_ANALYTICS",
        "OPENSEARCH_MANAGED_CLUSTER",
        "S3_VECTORS",
    )
)


def serialize_json(value: KnowledgeBaseStorageType) -> str:
    return value


def deserialize_json(data: str) -> KnowledgeBaseStorageType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown KnowledgeBaseStorageType value: {data!r}")
    return cast(KnowledgeBaseStorageType, data)
