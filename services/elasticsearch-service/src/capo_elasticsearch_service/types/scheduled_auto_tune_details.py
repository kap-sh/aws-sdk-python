"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ScheduledAutoTuneDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.auto_tune_date
    import capo_elasticsearch_service.types.scheduled_auto_tune_action_type
    import capo_elasticsearch_service.types.scheduled_auto_tune_description
    import capo_elasticsearch_service.types.scheduled_auto_tune_severity_type


class ScheduledAutoTuneDetails(TypedDict, closed=True):
    date: NotRequired["capo_elasticsearch_service.types.auto_tune_date.AutoTuneDate"]
    """<p>Specifies timestamp for the Auto-Tune action scheduled for the domain. </p>"""
    action_type: NotRequired[
        "capo_elasticsearch_service.types.scheduled_auto_tune_action_type.ScheduledAutoTuneActionType"
    ]
    """<p>Specifies Auto-Tune action type. Valid values are JVM_HEAP_SIZE_TUNING and JVM_YOUNG_GEN_TUNING. </p>"""
    action: NotRequired[
        "capo_elasticsearch_service.types.scheduled_auto_tune_description.ScheduledAutoTuneDescription"
    ]
    """<p>Specifies Auto-Tune action description. </p>"""
    severity: NotRequired[
        "capo_elasticsearch_service.types.scheduled_auto_tune_severity_type.ScheduledAutoTuneSeverityType"
    ]
    """<p>Specifies Auto-Tune action severity. Valid values are LOW, MEDIUM and HIGH. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScheduledAutoTuneDetails) -> dict:
    out: dict = {}
    if "date" in value:
        import capo_elasticsearch_service.types.auto_tune_date

        out["Date"] = capo_elasticsearch_service.types.auto_tune_date.serialize_json(
            value["date"]
        )
    if "action_type" in value:
        import capo_elasticsearch_service.types.scheduled_auto_tune_action_type

        out["ActionType"] = (
            capo_elasticsearch_service.types.scheduled_auto_tune_action_type.serialize_json(
                value["action_type"]
            )
        )
    if "action" in value:
        out["Action"] = value["action"]
    if "severity" in value:
        import capo_elasticsearch_service.types.scheduled_auto_tune_severity_type

        out["Severity"] = (
            capo_elasticsearch_service.types.scheduled_auto_tune_severity_type.serialize_json(
                value["severity"]
            )
        )
    return out


def deserialize_json(data: dict) -> ScheduledAutoTuneDetails:
    out: ScheduledAutoTuneDetails = {}  # type: ignore[typeddict-item]
    if "Date" in data:
        import capo_elasticsearch_service.types.auto_tune_date

        out["date"] = capo_elasticsearch_service.types.auto_tune_date.deserialize_json(
            data["Date"]
        )
    if "ActionType" in data:
        import capo_elasticsearch_service.types.scheduled_auto_tune_action_type

        out["action_type"] = (
            capo_elasticsearch_service.types.scheduled_auto_tune_action_type.deserialize_json(
                data["ActionType"]
            )
        )
    if "Action" in data:
        out["action"] = data["Action"]
    if "Severity" in data:
        import capo_elasticsearch_service.types.scheduled_auto_tune_severity_type

        out["severity"] = (
            capo_elasticsearch_service.types.scheduled_auto_tune_severity_type.deserialize_json(
                data["Severity"]
            )
        )
    return out
