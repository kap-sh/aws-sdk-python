"""Generated from Smithy shape ``com.amazonaws.kendra#SalesforceKnowledgeArticleState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

SalesforceKnowledgeArticleState: TypeAlias = Literal[
    "DRAFT",
    "PUBLISHED",
    "ARCHIVED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DRAFT",
        "PUBLISHED",
        "ARCHIVED",
    )
)


def serialize_aws_json_1_1(value: SalesforceKnowledgeArticleState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SalesforceKnowledgeArticleState:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SalesforceKnowledgeArticleState value: {data!r}"
        )
    return cast(SalesforceKnowledgeArticleState, data)
