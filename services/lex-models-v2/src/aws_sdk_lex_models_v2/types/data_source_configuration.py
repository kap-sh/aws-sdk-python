"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DataSourceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bedrock_knowledge_store_configuration
    import aws_sdk_lex_models_v2.types.opensearch_configuration
    import aws_sdk_lex_models_v2.types.qn_a_kendra_configuration


class DataSourceConfiguration(TypedDict, closed=True):
    opensearch_configuration: NotRequired[
        "aws_sdk_lex_models_v2.types.opensearch_configuration.OpensearchConfiguration"
    ]
    r"""<p>Contains details about the configuration of the Amazon OpenSearch Service database used for the <code>AMAZON.QnAIntent</code>. To create a domain, follow the steps at <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html\">Creating and managing Amazon OpenSearch Service domains</a>.</p>"""
    kendra_configuration: NotRequired[
        "aws_sdk_lex_models_v2.types.qn_a_kendra_configuration.QnAKendraConfiguration"
    ]
    r"""<p>Contains details about the configuration of the Amazon Kendra index used for the <code>AMAZON.QnAIntent</code>. To create a Amazon Kendra index, follow the steps at <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/create-index.html\">Creating an index</a>.</p>"""
    bedrock_knowledge_store_configuration: NotRequired[
        "aws_sdk_lex_models_v2.types.bedrock_knowledge_store_configuration.BedrockKnowledgeStoreConfiguration"
    ]
    r"""<p>Contains details about the configuration of the Amazon Bedrock knowledge base used for the <code>AMAZON.QnAIntent</code>. To set up a knowledge base, follow the steps at <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html\">Building a knowledge base</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceConfiguration) -> dict:
    out: dict = {}
    if "opensearch_configuration" in value:
        import aws_sdk_lex_models_v2.types.opensearch_configuration

        out["opensearchConfiguration"] = (
            aws_sdk_lex_models_v2.types.opensearch_configuration.serialize_json(
                value["opensearch_configuration"]
            )
        )
    if "kendra_configuration" in value:
        import aws_sdk_lex_models_v2.types.qn_a_kendra_configuration

        out["kendraConfiguration"] = (
            aws_sdk_lex_models_v2.types.qn_a_kendra_configuration.serialize_json(
                value["kendra_configuration"]
            )
        )
    if "bedrock_knowledge_store_configuration" in value:
        import aws_sdk_lex_models_v2.types.bedrock_knowledge_store_configuration

        out["bedrockKnowledgeStoreConfiguration"] = (
            aws_sdk_lex_models_v2.types.bedrock_knowledge_store_configuration.serialize_json(
                value["bedrock_knowledge_store_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataSourceConfiguration:
    out: DataSourceConfiguration = {}  # type: ignore[typeddict-item]
    if "opensearchConfiguration" in data:
        import aws_sdk_lex_models_v2.types.opensearch_configuration

        out["opensearch_configuration"] = (
            aws_sdk_lex_models_v2.types.opensearch_configuration.deserialize_json(
                data["opensearchConfiguration"]
            )
        )
    if "kendraConfiguration" in data:
        import aws_sdk_lex_models_v2.types.qn_a_kendra_configuration

        out["kendra_configuration"] = (
            aws_sdk_lex_models_v2.types.qn_a_kendra_configuration.deserialize_json(
                data["kendraConfiguration"]
            )
        )
    if "bedrockKnowledgeStoreConfiguration" in data:
        import aws_sdk_lex_models_v2.types.bedrock_knowledge_store_configuration

        out["bedrock_knowledge_store_configuration"] = (
            aws_sdk_lex_models_v2.types.bedrock_knowledge_store_configuration.deserialize_json(
                data["bedrockKnowledgeStoreConfiguration"]
            )
        )
    return out
