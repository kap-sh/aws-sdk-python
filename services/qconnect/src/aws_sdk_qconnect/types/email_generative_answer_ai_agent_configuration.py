"""Generated from Smithy shape ``com.amazonaws.qconnect#EmailGenerativeAnswerAIAgentConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.association_configuration_list
    import aws_sdk_qconnect.types.non_empty_string
    import aws_sdk_qconnect.types.uuid_with_qualifier


class EmailGenerativeAnswerAIAgentConfiguration(TypedDict):
    email_generative_answer_ai_prompt_id: NotRequired[
        "aws_sdk_qconnect.types.uuid_with_qualifier.UuidWithQualifier"
    ]
    """<p>The ID of the System AI prompt used for generating comprehensive knowledge-based answers from email queries.</p>"""
    email_query_reformulation_ai_prompt_id: NotRequired[
        "aws_sdk_qconnect.types.uuid_with_qualifier.UuidWithQualifier"
    ]
    """<p>The ID of the System AI prompt used for reformulating email queries to optimize knowledge base search results.</p>"""
    locale: NotRequired["aws_sdk_qconnect.types.non_empty_string.NonEmptyString"]
    """<p>The locale setting for language-specific email processing and response generation (for example, en_US, es_ES).</p>"""
    association_configurations: NotRequired[
        "aws_sdk_qconnect.types.association_configuration_list.AssociationConfigurationList"
    ]
    """<p>Configuration settings for knowledge base associations used by the email generative answer agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EmailGenerativeAnswerAIAgentConfiguration) -> dict:
    out: dict = {}
    if "email_generative_answer_ai_prompt_id" in value:
        out["emailGenerativeAnswerAIPromptId"] = value[
            "email_generative_answer_ai_prompt_id"
        ]
    if "email_query_reformulation_ai_prompt_id" in value:
        out["emailQueryReformulationAIPromptId"] = value[
            "email_query_reformulation_ai_prompt_id"
        ]
    if "locale" in value:
        out["locale"] = value["locale"]
    if "association_configurations" in value:
        import aws_sdk_qconnect.types.association_configuration_list

        out["associationConfigurations"] = (
            aws_sdk_qconnect.types.association_configuration_list.serialize_json(
                value["association_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> EmailGenerativeAnswerAIAgentConfiguration:
    out: EmailGenerativeAnswerAIAgentConfiguration = {}  # type: ignore[typeddict-item]
    if "emailGenerativeAnswerAIPromptId" in data:
        out["email_generative_answer_ai_prompt_id"] = data[
            "emailGenerativeAnswerAIPromptId"
        ]
    if "emailQueryReformulationAIPromptId" in data:
        out["email_query_reformulation_ai_prompt_id"] = data[
            "emailQueryReformulationAIPromptId"
        ]
    if "locale" in data:
        out["locale"] = data["locale"]
    if "associationConfigurations" in data:
        import aws_sdk_qconnect.types.association_configuration_list

        out["association_configurations"] = (
            aws_sdk_qconnect.types.association_configuration_list.deserialize_json(
                data["associationConfigurations"]
            )
        )
    return out
