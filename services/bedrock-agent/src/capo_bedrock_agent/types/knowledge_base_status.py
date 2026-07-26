"""Generated from Smithy shape ``com.amazonaws.bedrockagent#KnowledgeBaseStatus``."""

from typing import Literal, TypeAlias, cast

KnowledgeBaseStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "DELETING",
    "UPDATING",
    "FAILED",
    "DELETE_UNSUCCESSFUL",
]


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseStatus) -> str:
    return value


def deserialize_json(data: str) -> KnowledgeBaseStatus:
    return cast(KnowledgeBaseStatus, data)
