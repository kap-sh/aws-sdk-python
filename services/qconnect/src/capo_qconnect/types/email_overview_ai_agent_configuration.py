"""Generated from Smithy shape ``com.amazonaws.qconnect#EmailOverviewAIAgentConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.non_empty_string
    import capo_qconnect.types.uuid_with_qualifier


class EmailOverviewAIAgentConfiguration(TypedDict, closed=True):
    email_overview_ai_prompt_id: NotRequired[
        "capo_qconnect.types.uuid_with_qualifier.UuidWithQualifier"
    ]
    """<p>The ID of the System AI prompt used for generating structured email conversation summaries.</p>"""
    locale: NotRequired["capo_qconnect.types.non_empty_string.NonEmptyString"]
    """<p>The locale setting for language-specific email overview processing (for example, en_US, es_ES).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EmailOverviewAIAgentConfiguration) -> dict:
    out: dict = {}
    if "email_overview_ai_prompt_id" in value:
        out["emailOverviewAIPromptId"] = value["email_overview_ai_prompt_id"]
    if "locale" in value:
        out["locale"] = value["locale"]
    return out


def deserialize_json(data: dict) -> EmailOverviewAIAgentConfiguration:
    out: EmailOverviewAIAgentConfiguration = {}  # type: ignore[typeddict-item]
    if "emailOverviewAIPromptId" in data:
        out["email_overview_ai_prompt_id"] = data["emailOverviewAIPromptId"]
    if "locale" in data:
        out["locale"] = data["locale"]
    return out
