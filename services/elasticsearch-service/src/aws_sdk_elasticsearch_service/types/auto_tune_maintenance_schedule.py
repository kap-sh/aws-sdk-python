"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#AutoTuneMaintenanceSchedule``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.duration
    import aws_sdk_elasticsearch_service.types.start_at
    import aws_sdk_elasticsearch_service.types.string


class AutoTuneMaintenanceSchedule(TypedDict):
    start_at: NotRequired["aws_sdk_elasticsearch_service.types.start_at.StartAt"]
    """<p>Specifies timestamp at which Auto-Tune maintenance schedule start. </p>"""
    duration: NotRequired["aws_sdk_elasticsearch_service.types.duration.Duration"]
    r"""<p>Specifies maintenance schedule duration: duration value and duration unit. See the <a href=\"https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/auto-tune.html\" target=\"_blank\">Developer Guide</a> for more information.</p>"""
    cron_expression_for_recurrence: NotRequired[
        "aws_sdk_elasticsearch_service.types.string.String"
    ]
    r"""<p>Specifies cron expression for a recurring maintenance schedule. See the <a href=\"https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/auto-tune.html\" target=\"_blank\">Developer Guide</a> for more information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutoTuneMaintenanceSchedule) -> dict:
    out: dict = {}
    if "start_at" in value:
        import aws_sdk_elasticsearch_service.types.start_at

        out["StartAt"] = aws_sdk_elasticsearch_service.types.start_at.serialize_json(
            value["start_at"]
        )
    if "duration" in value:
        import aws_sdk_elasticsearch_service.types.duration

        out["Duration"] = aws_sdk_elasticsearch_service.types.duration.serialize_json(
            value["duration"]
        )
    if "cron_expression_for_recurrence" in value:
        out["CronExpressionForRecurrence"] = value["cron_expression_for_recurrence"]
    return out


def deserialize_json(data: dict) -> AutoTuneMaintenanceSchedule:
    out: AutoTuneMaintenanceSchedule = {}  # type: ignore[typeddict-item]
    if "StartAt" in data:
        import aws_sdk_elasticsearch_service.types.start_at

        out["start_at"] = aws_sdk_elasticsearch_service.types.start_at.deserialize_json(
            data["StartAt"]
        )
    if "Duration" in data:
        import aws_sdk_elasticsearch_service.types.duration

        out["duration"] = aws_sdk_elasticsearch_service.types.duration.deserialize_json(
            data["Duration"]
        )
    if "CronExpressionForRecurrence" in data:
        out["cron_expression_for_recurrence"] = data["CronExpressionForRecurrence"]
    return out
