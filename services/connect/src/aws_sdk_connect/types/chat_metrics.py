"""Generated from Smithy shape ``com.amazonaws.connect#ChatMetrics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.chat_contact_metrics
    import aws_sdk_connect.types.participant_metrics


class ChatMetrics(TypedDict, closed=True):
    chat_contact_metrics: NotRequired[
        "aws_sdk_connect.types.chat_contact_metrics.ChatContactMetrics"
    ]
    """<p>Information about the overall participant interactions at the contact level.</p>"""
    agent_metrics: NotRequired[
        "aws_sdk_connect.types.participant_metrics.ParticipantMetrics"
    ]
    """<p>Information about agent interactions in a contact.</p>"""
    customer_metrics: NotRequired[
        "aws_sdk_connect.types.participant_metrics.ParticipantMetrics"
    ]
    """<p>Information about customer interactions in a contact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChatMetrics) -> dict:
    out: dict = {}
    if "chat_contact_metrics" in value:
        import aws_sdk_connect.types.chat_contact_metrics

        out["ChatContactMetrics"] = (
            aws_sdk_connect.types.chat_contact_metrics.serialize_json(
                value["chat_contact_metrics"]
            )
        )
    if "agent_metrics" in value:
        import aws_sdk_connect.types.participant_metrics

        out["AgentMetrics"] = aws_sdk_connect.types.participant_metrics.serialize_json(
            value["agent_metrics"]
        )
    if "customer_metrics" in value:
        import aws_sdk_connect.types.participant_metrics

        out["CustomerMetrics"] = (
            aws_sdk_connect.types.participant_metrics.serialize_json(
                value["customer_metrics"]
            )
        )
    return out


def deserialize_json(data: dict) -> ChatMetrics:
    out: ChatMetrics = {}  # type: ignore[typeddict-item]
    if "ChatContactMetrics" in data:
        import aws_sdk_connect.types.chat_contact_metrics

        out["chat_contact_metrics"] = (
            aws_sdk_connect.types.chat_contact_metrics.deserialize_json(
                data["ChatContactMetrics"]
            )
        )
    if "AgentMetrics" in data:
        import aws_sdk_connect.types.participant_metrics

        out["agent_metrics"] = (
            aws_sdk_connect.types.participant_metrics.deserialize_json(
                data["AgentMetrics"]
            )
        )
    if "CustomerMetrics" in data:
        import aws_sdk_connect.types.participant_metrics

        out["customer_metrics"] = (
            aws_sdk_connect.types.participant_metrics.deserialize_json(
                data["CustomerMetrics"]
            )
        )
    return out
