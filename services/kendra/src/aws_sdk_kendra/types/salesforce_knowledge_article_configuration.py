"""Generated from Smithy shape ``com.amazonaws.kendra#SalesforceKnowledgeArticleConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.salesforce_custom_knowledge_article_type_configuration_list
    import aws_sdk_kendra.types.salesforce_knowledge_article_state_list
    import aws_sdk_kendra.types.salesforce_standard_knowledge_article_type_configuration


class SalesforceKnowledgeArticleConfiguration(TypedDict, closed=True):
    included_states: "aws_sdk_kendra.types.salesforce_knowledge_article_state_list.SalesforceKnowledgeArticleStateList"
    """<p>Specifies the document states that should be included when Amazon Kendra indexes knowledge articles. You must specify at least one state.</p>"""
    standard_knowledge_article_type_configuration: NotRequired[
        "aws_sdk_kendra.types.salesforce_standard_knowledge_article_type_configuration.SalesforceStandardKnowledgeArticleTypeConfiguration"
    ]
    """<p>Configuration information for standard Salesforce knowledge articles.</p>"""
    custom_knowledge_article_type_configurations: NotRequired[
        "aws_sdk_kendra.types.salesforce_custom_knowledge_article_type_configuration_list.SalesforceCustomKnowledgeArticleTypeConfigurationList"
    ]
    """<p>Configuration information for custom Salesforce knowledge articles.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SalesforceKnowledgeArticleConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_kendra.types.salesforce_knowledge_article_state_list

    out["IncludedStates"] = (
        aws_sdk_kendra.types.salesforce_knowledge_article_state_list.serialize_aws_json_1_1(
            value["included_states"]
        )
    )
    if "standard_knowledge_article_type_configuration" in value:
        import aws_sdk_kendra.types.salesforce_standard_knowledge_article_type_configuration

        out["StandardKnowledgeArticleTypeConfiguration"] = (
            aws_sdk_kendra.types.salesforce_standard_knowledge_article_type_configuration.serialize_aws_json_1_1(
                value["standard_knowledge_article_type_configuration"]
            )
        )
    if "custom_knowledge_article_type_configurations" in value:
        import aws_sdk_kendra.types.salesforce_custom_knowledge_article_type_configuration_list

        out["CustomKnowledgeArticleTypeConfigurations"] = (
            aws_sdk_kendra.types.salesforce_custom_knowledge_article_type_configuration_list.serialize_aws_json_1_1(
                value["custom_knowledge_article_type_configurations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SalesforceKnowledgeArticleConfiguration:
    out: SalesforceKnowledgeArticleConfiguration = {}  # type: ignore[typeddict-item]
    if "IncludedStates" in data:
        import aws_sdk_kendra.types.salesforce_knowledge_article_state_list

        out["included_states"] = (
            aws_sdk_kendra.types.salesforce_knowledge_article_state_list.deserialize_aws_json_1_1(
                data["IncludedStates"]
            )
        )
    else:
        raise DeserializationError(
            "SalesforceKnowledgeArticleConfiguration.included_states required"
        )
    if "StandardKnowledgeArticleTypeConfiguration" in data:
        import aws_sdk_kendra.types.salesforce_standard_knowledge_article_type_configuration

        out["standard_knowledge_article_type_configuration"] = (
            aws_sdk_kendra.types.salesforce_standard_knowledge_article_type_configuration.deserialize_aws_json_1_1(
                data["StandardKnowledgeArticleTypeConfiguration"]
            )
        )
    if "CustomKnowledgeArticleTypeConfigurations" in data:
        import aws_sdk_kendra.types.salesforce_custom_knowledge_article_type_configuration_list

        out["custom_knowledge_article_type_configurations"] = (
            aws_sdk_kendra.types.salesforce_custom_knowledge_article_type_configuration_list.deserialize_aws_json_1_1(
                data["CustomKnowledgeArticleTypeConfigurations"]
            )
        )
    return out
