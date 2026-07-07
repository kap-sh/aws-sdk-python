"""Generated from Smithy shape ``com.amazonaws.bedrockagent#KnowledgeBaseFlowNodeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.flow_knowledge_base_id
    import aws_sdk_bedrock_agent.types.guardrail_configuration
    import aws_sdk_bedrock_agent.types.knowledge_base_model_identifier
    import aws_sdk_bedrock_agent.types.knowledge_base_orchestration_configuration
    import aws_sdk_bedrock_agent.types.knowledge_base_prompt_template
    import aws_sdk_bedrock_agent.types.prompt_inference_configuration
    import aws_sdk_bedrock_agent.types.vector_search_reranking_configuration


class KnowledgeBaseFlowNodeConfiguration(TypedDict, closed=True):
    knowledge_base_id: (
        "aws_sdk_bedrock_agent.types.flow_knowledge_base_id.FlowKnowledgeBaseId"
    )
    """<p>The unique identifier of the knowledge base to query.</p>"""
    model_id: NotRequired[
        "aws_sdk_bedrock_agent.types.knowledge_base_model_identifier.KnowledgeBaseModelIdentifier"
    ]
    r"""<p>The unique identifier of the model or <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html\">inference profile</a> to use to generate a response from the query results. Omit this field if you want to return the retrieved results as an array.</p>"""
    guardrail_configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.guardrail_configuration.GuardrailConfiguration"
    ]
    """<p>Contains configurations for a guardrail to apply during query and response generation for the knowledge base in this configuration.</p>"""
    number_of_results: NotRequired["int"]
    """<p>The number of results to retrieve from the knowledge base.</p>"""
    prompt_template: NotRequired[
        "aws_sdk_bedrock_agent.types.knowledge_base_prompt_template.KnowledgeBasePromptTemplate"
    ]
    """<p>A custom prompt template to use with the knowledge base for generating responses.</p>"""
    inference_configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.prompt_inference_configuration.PromptInferenceConfiguration"
    ]
    """<p>Contains inference configurations for the prompt.</p>"""
    reranking_configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.vector_search_reranking_configuration.VectorSearchRerankingConfiguration"
    ]
    """<p>The configuration for reranking the retrieved results from the knowledge base to improve relevance.</p>"""
    orchestration_configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.knowledge_base_orchestration_configuration.KnowledgeBaseOrchestrationConfiguration"
    ]
    """<p>The configuration for orchestrating the retrieval and generation process in the knowledge base node.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseFlowNodeConfiguration) -> dict:
    out: dict = {}
    out["knowledgeBaseId"] = value.get("knowledge_base_id", "")
    if "model_id" in value:
        out["modelId"] = value["model_id"]
    if "guardrail_configuration" in value:
        import aws_sdk_bedrock_agent.types.guardrail_configuration

        out["guardrailConfiguration"] = (
            aws_sdk_bedrock_agent.types.guardrail_configuration.serialize_json(
                value["guardrail_configuration"]
            )
        )
    if "number_of_results" in value:
        out["numberOfResults"] = value["number_of_results"]
    if "prompt_template" in value:
        import aws_sdk_bedrock_agent.types.knowledge_base_prompt_template

        out["promptTemplate"] = (
            aws_sdk_bedrock_agent.types.knowledge_base_prompt_template.serialize_json(
                value["prompt_template"]
            )
        )
    if "inference_configuration" in value:
        import aws_sdk_bedrock_agent.types.prompt_inference_configuration

        out["inferenceConfiguration"] = (
            aws_sdk_bedrock_agent.types.prompt_inference_configuration.serialize_json(
                value["inference_configuration"]
            )
        )
    if "reranking_configuration" in value:
        import aws_sdk_bedrock_agent.types.vector_search_reranking_configuration

        out["rerankingConfiguration"] = (
            aws_sdk_bedrock_agent.types.vector_search_reranking_configuration.serialize_json(
                value["reranking_configuration"]
            )
        )
    if "orchestration_configuration" in value:
        import aws_sdk_bedrock_agent.types.knowledge_base_orchestration_configuration

        out["orchestrationConfiguration"] = (
            aws_sdk_bedrock_agent.types.knowledge_base_orchestration_configuration.serialize_json(
                value["orchestration_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> KnowledgeBaseFlowNodeConfiguration:
    out: KnowledgeBaseFlowNodeConfiguration = {}  # type: ignore[typeddict-item]
    if "knowledgeBaseId" in data:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    else:
        out["knowledge_base_id"] = ""
    if "modelId" in data:
        out["model_id"] = data["modelId"]
    if "guardrailConfiguration" in data:
        import aws_sdk_bedrock_agent.types.guardrail_configuration

        out["guardrail_configuration"] = (
            aws_sdk_bedrock_agent.types.guardrail_configuration.deserialize_json(
                data["guardrailConfiguration"]
            )
        )
    if "numberOfResults" in data:
        out["number_of_results"] = data["numberOfResults"]
    if "promptTemplate" in data:
        import aws_sdk_bedrock_agent.types.knowledge_base_prompt_template

        out["prompt_template"] = (
            aws_sdk_bedrock_agent.types.knowledge_base_prompt_template.deserialize_json(
                data["promptTemplate"]
            )
        )
    if "inferenceConfiguration" in data:
        import aws_sdk_bedrock_agent.types.prompt_inference_configuration

        out["inference_configuration"] = (
            aws_sdk_bedrock_agent.types.prompt_inference_configuration.deserialize_json(
                data["inferenceConfiguration"]
            )
        )
    if "rerankingConfiguration" in data:
        import aws_sdk_bedrock_agent.types.vector_search_reranking_configuration

        out["reranking_configuration"] = (
            aws_sdk_bedrock_agent.types.vector_search_reranking_configuration.deserialize_json(
                data["rerankingConfiguration"]
            )
        )
    if "orchestrationConfiguration" in data:
        import aws_sdk_bedrock_agent.types.knowledge_base_orchestration_configuration

        out["orchestration_configuration"] = (
            aws_sdk_bedrock_agent.types.knowledge_base_orchestration_configuration.deserialize_json(
                data["orchestrationConfiguration"]
            )
        )
    return out
