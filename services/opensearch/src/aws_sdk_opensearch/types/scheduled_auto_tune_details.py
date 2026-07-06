"""Generated from Smithy shape ``com.amazonaws.opensearch#ScheduledAutoTuneDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.auto_tune_date
    import aws_sdk_opensearch.types.scheduled_auto_tune_action_type
    import aws_sdk_opensearch.types.scheduled_auto_tune_description
    import aws_sdk_opensearch.types.scheduled_auto_tune_severity_type


class ScheduledAutoTuneDetails(TypedDict, closed=True):
    date: NotRequired["aws_sdk_opensearch.types.auto_tune_date.AutoTuneDate"]
    """<p>The date and time when the Auto-Tune action is scheduled for the domain.</p>"""
    action_type: NotRequired[
        "aws_sdk_opensearch.types.scheduled_auto_tune_action_type.ScheduledAutoTuneActionType"
    ]
    """<p>The type of Auto-Tune action.</p>"""
    action: NotRequired[
        "aws_sdk_opensearch.types.scheduled_auto_tune_description.ScheduledAutoTuneDescription"
    ]
    """<p>A description of the Auto-Tune action.</p>"""
    severity: NotRequired[
        "aws_sdk_opensearch.types.scheduled_auto_tune_severity_type.ScheduledAutoTuneSeverityType"
    ]
    """<p>The severity of the Auto-Tune action. Valid values are <code>LOW</code>, <code>MEDIUM</code>, and <code>HIGH</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScheduledAutoTuneDetails) -> dict:
    out: dict = {}
    if "date" in value:
        import aws_sdk_opensearch.types.auto_tune_date

        out["Date"] = aws_sdk_opensearch.types.auto_tune_date.serialize_json(
            value["date"]
        )
    if "action_type" in value:
        import aws_sdk_opensearch.types.scheduled_auto_tune_action_type

        out["ActionType"] = (
            aws_sdk_opensearch.types.scheduled_auto_tune_action_type.serialize_json(
                value["action_type"]
            )
        )
    if "action" in value:
        out["Action"] = value["action"]
    if "severity" in value:
        import aws_sdk_opensearch.types.scheduled_auto_tune_severity_type

        out["Severity"] = (
            aws_sdk_opensearch.types.scheduled_auto_tune_severity_type.serialize_json(
                value["severity"]
            )
        )
    return out


def deserialize_json(data: dict) -> ScheduledAutoTuneDetails:
    out: ScheduledAutoTuneDetails = {}  # type: ignore[typeddict-item]
    if "Date" in data:
        import aws_sdk_opensearch.types.auto_tune_date

        out["date"] = aws_sdk_opensearch.types.auto_tune_date.deserialize_json(
            data["Date"]
        )
    if "ActionType" in data:
        import aws_sdk_opensearch.types.scheduled_auto_tune_action_type

        out["action_type"] = (
            aws_sdk_opensearch.types.scheduled_auto_tune_action_type.deserialize_json(
                data["ActionType"]
            )
        )
    if "Action" in data:
        out["action"] = data["Action"]
    if "Severity" in data:
        import aws_sdk_opensearch.types.scheduled_auto_tune_severity_type

        out["severity"] = (
            aws_sdk_opensearch.types.scheduled_auto_tune_severity_type.deserialize_json(
                data["Severity"]
            )
        )
    return out
