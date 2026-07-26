"""Generated from Smithy shape ``com.amazonaws.kendra#SalesforceCustomKnowledgeArticleTypeConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.salesforce_custom_knowledge_article_type_configuration

SalesforceCustomKnowledgeArticleTypeConfigurationList: TypeAlias = list[
    "capo_kendra.types.salesforce_custom_knowledge_article_type_configuration.SalesforceCustomKnowledgeArticleTypeConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: SalesforceCustomKnowledgeArticleTypeConfigurationList,
) -> list:
    import capo_kendra.types.salesforce_custom_knowledge_article_type_configuration

    out: list = []
    for item in value:
        out.append(
            capo_kendra.types.salesforce_custom_knowledge_article_type_configuration.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: list,
) -> SalesforceCustomKnowledgeArticleTypeConfigurationList:
    import capo_kendra.types.salesforce_custom_knowledge_article_type_configuration

    out: SalesforceCustomKnowledgeArticleTypeConfigurationList = []
    for item in data:
        out.append(
            capo_kendra.types.salesforce_custom_knowledge_article_type_configuration.deserialize_aws_json_1_1(
                item
            )
        )
    return out
