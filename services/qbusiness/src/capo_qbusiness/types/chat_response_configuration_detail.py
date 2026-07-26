"""Generated from Smithy shape ``com.amazonaws.qbusiness#ChatResponseConfigurationDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.chat_response_configuration_status
    import capo_qbusiness.types.error_detail
    import capo_qbusiness.types.response_configurations
    import capo_qbusiness.types.string
    import capo_qbusiness.types.timestamp


class ChatResponseConfigurationDetail(TypedDict, closed=True):
    response_configurations: NotRequired[
        "capo_qbusiness.types.response_configurations.ResponseConfigurations"
    ]
    """<p>A collection of specific response configuration settings that collectively define how responses are generated, formatted, and presented to users in chat interactions.</p>"""
    response_configuration_summary: NotRequired["capo_qbusiness.types.string.String"]
    """<p>A summary of the response configuration details, providing a concise overview of the key parameters and settings that define the response generation behavior.</p>"""
    status: NotRequired[
        "capo_qbusiness.types.chat_response_configuration_status.ChatResponseConfigurationStatus"
    ]
    """<p>The current status of the chat response configuration, indicating whether it is active, pending, or in another state that affects its availability for use.</p>"""
    error: NotRequired["capo_qbusiness.types.error_detail.ErrorDetail"]
    updated_at: NotRequired["capo_qbusiness.types.timestamp.Timestamp"]
    """<p>The timestamp indicating when the detailed chat response configuration was last modified, helping administrators track changes and maintain version awareness.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChatResponseConfigurationDetail) -> dict:
    out: dict = {}
    if "response_configurations" in value:
        import capo_qbusiness.types.response_configurations

        out["responseConfigurations"] = (
            capo_qbusiness.types.response_configurations.serialize_json(
                value["response_configurations"]
            )
        )
    if "response_configuration_summary" in value:
        out["responseConfigurationSummary"] = value["response_configuration_summary"]
    if "status" in value:
        import capo_qbusiness.types.chat_response_configuration_status

        out["status"] = (
            capo_qbusiness.types.chat_response_configuration_status.serialize_json(
                value["status"]
            )
        )
    if "error" in value:
        import capo_qbusiness.types.error_detail

        out["error"] = capo_qbusiness.types.error_detail.serialize_json(value["error"])
    if "updated_at" in value:
        import capo_qbusiness.types.timestamp

        out["updatedAt"] = capo_qbusiness.types.timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> ChatResponseConfigurationDetail:
    out: ChatResponseConfigurationDetail = {}  # type: ignore[typeddict-item]
    if "responseConfigurations" in data:
        import capo_qbusiness.types.response_configurations

        out["response_configurations"] = (
            capo_qbusiness.types.response_configurations.deserialize_json(
                data["responseConfigurations"]
            )
        )
    if "responseConfigurationSummary" in data:
        out["response_configuration_summary"] = data["responseConfigurationSummary"]
    if "status" in data:
        import capo_qbusiness.types.chat_response_configuration_status

        out["status"] = (
            capo_qbusiness.types.chat_response_configuration_status.deserialize_json(
                data["status"]
            )
        )
    if "error" in data:
        import capo_qbusiness.types.error_detail

        out["error"] = capo_qbusiness.types.error_detail.deserialize_json(data["error"])
    if "updatedAt" in data:
        import capo_qbusiness.types.timestamp

        out["updated_at"] = capo_qbusiness.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    return out
