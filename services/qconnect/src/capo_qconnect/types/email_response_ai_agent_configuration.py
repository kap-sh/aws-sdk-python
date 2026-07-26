"""Generated from Smithy shape ``com.amazonaws.qconnect#EmailResponseAIAgentConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.association_configuration_list
    import capo_qconnect.types.non_empty_string
    import capo_qconnect.types.uuid_with_qualifier


class EmailResponseAIAgentConfiguration(TypedDict, closed=True):
    email_response_ai_prompt_id: NotRequired[
        "capo_qconnect.types.uuid_with_qualifier.UuidWithQualifier"
    ]
    """<p>The ID of the System AI prompt used for generating professional email responses based on knowledge base content.</p>"""
    email_query_reformulation_ai_prompt_id: NotRequired[
        "capo_qconnect.types.uuid_with_qualifier.UuidWithQualifier"
    ]
    """<p>The ID of the System AI prompt used for reformulating email queries to optimize knowledge base search for response generation.</p>"""
    locale: NotRequired["capo_qconnect.types.non_empty_string.NonEmptyString"]
    """<p>The locale setting for language-specific email response generation (for example, en_US, es_ES).</p>"""
    association_configurations: NotRequired[
        "capo_qconnect.types.association_configuration_list.AssociationConfigurationList"
    ]
    """<p>Configuration settings for knowledge base associations used by the email response agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EmailResponseAIAgentConfiguration) -> dict:
    out: dict = {}
    if "email_response_ai_prompt_id" in value:
        out["emailResponseAIPromptId"] = value["email_response_ai_prompt_id"]
    if "email_query_reformulation_ai_prompt_id" in value:
        out["emailQueryReformulationAIPromptId"] = value[
            "email_query_reformulation_ai_prompt_id"
        ]
    if "locale" in value:
        out["locale"] = value["locale"]
    if "association_configurations" in value:
        import capo_qconnect.types.association_configuration_list

        out["associationConfigurations"] = (
            capo_qconnect.types.association_configuration_list.serialize_json(
                value["association_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> EmailResponseAIAgentConfiguration:
    out: EmailResponseAIAgentConfiguration = {}  # type: ignore[typeddict-item]
    if "emailResponseAIPromptId" in data:
        out["email_response_ai_prompt_id"] = data["emailResponseAIPromptId"]
    if "emailQueryReformulationAIPromptId" in data:
        out["email_query_reformulation_ai_prompt_id"] = data[
            "emailQueryReformulationAIPromptId"
        ]
    if "locale" in data:
        out["locale"] = data["locale"]
    if "associationConfigurations" in data:
        import capo_qconnect.types.association_configuration_list

        out["association_configurations"] = (
            capo_qconnect.types.association_configuration_list.deserialize_json(
                data["associationConfigurations"]
            )
        )
    return out
