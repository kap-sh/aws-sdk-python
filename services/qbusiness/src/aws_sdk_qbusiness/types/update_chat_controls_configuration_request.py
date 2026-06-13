"""Generated from Smithy shape ``com.amazonaws.qbusiness#UpdateChatControlsConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.blocked_phrases_configuration_update
    import aws_sdk_qbusiness.types.client_token
    import aws_sdk_qbusiness.types.creator_mode_configuration
    import aws_sdk_qbusiness.types.hallucination_reduction_configuration
    import aws_sdk_qbusiness.types.orchestration_configuration
    import aws_sdk_qbusiness.types.response_scope
    import aws_sdk_qbusiness.types.topic_configurations


class UpdateChatControlsConfigurationRequest(TypedDict):
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the application for which the chat controls are configured.</p>"""
    client_token: NotRequired["aws_sdk_qbusiness.types.client_token.ClientToken"]
    """<p>A token that you provide to identify the request to update a Amazon Q Business application chat configuration.</p>"""
    response_scope: NotRequired["aws_sdk_qbusiness.types.response_scope.ResponseScope"]
    """<p>The response scope configured for your application. This determines whether your application uses its retrieval augmented generation (RAG) system to generate answers only from your enterprise data, or also uses the large language models (LLM) knowledge to respons to end user questions in chat.</p>"""
    orchestration_configuration: NotRequired[
        "aws_sdk_qbusiness.types.orchestration_configuration.OrchestrationConfiguration"
    ]
    """<p> The chat response orchestration settings for your application.</p>"""
    blocked_phrases_configuration_update: NotRequired[
        "aws_sdk_qbusiness.types.blocked_phrases_configuration_update.BlockedPhrasesConfigurationUpdate"
    ]
    """<p>The phrases blocked from chat by your chat control configuration.</p>"""
    topic_configurations_to_create_or_update: NotRequired[
        "aws_sdk_qbusiness.types.topic_configurations.TopicConfigurations"
    ]
    """<p>The configured topic specific chat controls you want to update.</p>"""
    topic_configurations_to_delete: NotRequired[
        "aws_sdk_qbusiness.types.topic_configurations.TopicConfigurations"
    ]
    """<p>The configured topic specific chat controls you want to delete.</p>"""
    creator_mode_configuration: NotRequired[
        "aws_sdk_qbusiness.types.creator_mode_configuration.CreatorModeConfiguration"
    ]
    """<p>The configuration details for <code>CREATOR_MODE</code>.</p>"""
    hallucination_reduction_configuration: NotRequired[
        "aws_sdk_qbusiness.types.hallucination_reduction_configuration.HallucinationReductionConfiguration"
    ]
    """<p> The hallucination reduction settings for your application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateChatControlsConfigurationRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "response_scope" in value:
        import aws_sdk_qbusiness.types.response_scope

        out["responseScope"] = aws_sdk_qbusiness.types.response_scope.serialize_json(
            value["response_scope"]
        )
    if "orchestration_configuration" in value:
        import aws_sdk_qbusiness.types.orchestration_configuration

        out["orchestrationConfiguration"] = (
            aws_sdk_qbusiness.types.orchestration_configuration.serialize_json(
                value["orchestration_configuration"]
            )
        )
    if "blocked_phrases_configuration_update" in value:
        import aws_sdk_qbusiness.types.blocked_phrases_configuration_update

        out["blockedPhrasesConfigurationUpdate"] = (
            aws_sdk_qbusiness.types.blocked_phrases_configuration_update.serialize_json(
                value["blocked_phrases_configuration_update"]
            )
        )
    if "topic_configurations_to_create_or_update" in value:
        import aws_sdk_qbusiness.types.topic_configurations

        out["topicConfigurationsToCreateOrUpdate"] = (
            aws_sdk_qbusiness.types.topic_configurations.serialize_json(
                value["topic_configurations_to_create_or_update"]
            )
        )
    if "topic_configurations_to_delete" in value:
        import aws_sdk_qbusiness.types.topic_configurations

        out["topicConfigurationsToDelete"] = (
            aws_sdk_qbusiness.types.topic_configurations.serialize_json(
                value["topic_configurations_to_delete"]
            )
        )
    if "creator_mode_configuration" in value:
        import aws_sdk_qbusiness.types.creator_mode_configuration

        out["creatorModeConfiguration"] = (
            aws_sdk_qbusiness.types.creator_mode_configuration.serialize_json(
                value["creator_mode_configuration"]
            )
        )
    if "hallucination_reduction_configuration" in value:
        import aws_sdk_qbusiness.types.hallucination_reduction_configuration

        out["hallucinationReductionConfiguration"] = (
            aws_sdk_qbusiness.types.hallucination_reduction_configuration.serialize_json(
                value["hallucination_reduction_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateChatControlsConfigurationRequest:
    out: UpdateChatControlsConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "responseScope" in data:
        import aws_sdk_qbusiness.types.response_scope

        out["response_scope"] = aws_sdk_qbusiness.types.response_scope.deserialize_json(
            data["responseScope"]
        )
    if "orchestrationConfiguration" in data:
        import aws_sdk_qbusiness.types.orchestration_configuration

        out["orchestration_configuration"] = (
            aws_sdk_qbusiness.types.orchestration_configuration.deserialize_json(
                data["orchestrationConfiguration"]
            )
        )
    if "blockedPhrasesConfigurationUpdate" in data:
        import aws_sdk_qbusiness.types.blocked_phrases_configuration_update

        out["blocked_phrases_configuration_update"] = (
            aws_sdk_qbusiness.types.blocked_phrases_configuration_update.deserialize_json(
                data["blockedPhrasesConfigurationUpdate"]
            )
        )
    if "topicConfigurationsToCreateOrUpdate" in data:
        import aws_sdk_qbusiness.types.topic_configurations

        out["topic_configurations_to_create_or_update"] = (
            aws_sdk_qbusiness.types.topic_configurations.deserialize_json(
                data["topicConfigurationsToCreateOrUpdate"]
            )
        )
    if "topicConfigurationsToDelete" in data:
        import aws_sdk_qbusiness.types.topic_configurations

        out["topic_configurations_to_delete"] = (
            aws_sdk_qbusiness.types.topic_configurations.deserialize_json(
                data["topicConfigurationsToDelete"]
            )
        )
    if "creatorModeConfiguration" in data:
        import aws_sdk_qbusiness.types.creator_mode_configuration

        out["creator_mode_configuration"] = (
            aws_sdk_qbusiness.types.creator_mode_configuration.deserialize_json(
                data["creatorModeConfiguration"]
            )
        )
    if "hallucinationReductionConfiguration" in data:
        import aws_sdk_qbusiness.types.hallucination_reduction_configuration

        out["hallucination_reduction_configuration"] = (
            aws_sdk_qbusiness.types.hallucination_reduction_configuration.deserialize_json(
                data["hallucinationReductionConfiguration"]
            )
        )
    return out
