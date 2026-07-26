"""Generated from Smithy shape ``com.amazonaws.bedrockagent#KnowledgeBaseStorageType``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: KnowledgeBaseStorageType) -> str:
    return value


def deserialize_json(data: str) -> KnowledgeBaseStorageType:
    return cast(KnowledgeBaseStorageType, data)
