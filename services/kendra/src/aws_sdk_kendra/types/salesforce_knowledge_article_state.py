"""Generated from Smithy shape ``com.amazonaws.kendra#SalesforceKnowledgeArticleState``."""

from typing import Literal, TypeAlias, cast

SalesforceKnowledgeArticleState: TypeAlias = Literal[
    "DRAFT",
    "PUBLISHED",
    "ARCHIVED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SalesforceKnowledgeArticleState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SalesforceKnowledgeArticleState:
    return cast(SalesforceKnowledgeArticleState, data)
