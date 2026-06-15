"""Generated from Smithy shape ``com.amazonaws.devopsguru#NotificationFilterConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.insight_severities
    import aws_sdk_devops_guru.types.notification_message_types


class NotificationFilterConfig(TypedDict):
    severities: NotRequired[
        "aws_sdk_devops_guru.types.insight_severities.InsightSeverities"
    ]
    r"""<p> The severity levels that you want to receive notifications for. For example, you can choose to receive notifications only for insights with <code>HIGH</code> and <code>MEDIUM</code> severity levels. For more information, see <a href=\"https://docs.aws.amazon.com/devops-guru/latest/userguide/working-with-insights.html#understanding-insights-severities\">Understanding insight severities</a>. </p>"""
    message_types: NotRequired[
        "aws_sdk_devops_guru.types.notification_message_types.NotificationMessageTypes"
    ]
    """<p> The events that you want to receive notifications for. For example, you can choose to receive notifications only when the severity level is upgraded or a new insight is created. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotificationFilterConfig) -> dict:
    out: dict = {}
    if "severities" in value:
        import aws_sdk_devops_guru.types.insight_severities

        out["Severities"] = aws_sdk_devops_guru.types.insight_severities.serialize_json(
            value["severities"]
        )
    if "message_types" in value:
        import aws_sdk_devops_guru.types.notification_message_types

        out["MessageTypes"] = (
            aws_sdk_devops_guru.types.notification_message_types.serialize_json(
                value["message_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> NotificationFilterConfig:
    out: NotificationFilterConfig = {}  # type: ignore[typeddict-item]
    if "Severities" in data:
        import aws_sdk_devops_guru.types.insight_severities

        out["severities"] = (
            aws_sdk_devops_guru.types.insight_severities.deserialize_json(
                data["Severities"]
            )
        )
    if "MessageTypes" in data:
        import aws_sdk_devops_guru.types.notification_message_types

        out["message_types"] = (
            aws_sdk_devops_guru.types.notification_message_types.deserialize_json(
                data["MessageTypes"]
            )
        )
    return out
