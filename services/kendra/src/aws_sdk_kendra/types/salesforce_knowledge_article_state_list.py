"""Generated from Smithy shape ``com.amazonaws.kendra#SalesforceKnowledgeArticleStateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.salesforce_knowledge_article_state

SalesforceKnowledgeArticleStateList: TypeAlias = list[
    "aws_sdk_kendra.types.salesforce_knowledge_article_state.SalesforceKnowledgeArticleState"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SalesforceKnowledgeArticleStateList) -> list:
    import aws_sdk_kendra.types.salesforce_knowledge_article_state

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kendra.types.salesforce_knowledge_article_state.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SalesforceKnowledgeArticleStateList:
    import aws_sdk_kendra.types.salesforce_knowledge_article_state

    out: SalesforceKnowledgeArticleStateList = []
    for item in data:
        out.append(
            aws_sdk_kendra.types.salesforce_knowledge_article_state.deserialize_aws_json_1_1(
                item
            )
        )
    return out
