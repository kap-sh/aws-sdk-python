"""Generated from Smithy shape ``com.amazonaws.iot#ScheduledAuditMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.audit_frequency
    import aws_sdk_iot.types.day_of_month
    import aws_sdk_iot.types.day_of_week
    import aws_sdk_iot.types.scheduled_audit_arn
    import aws_sdk_iot.types.scheduled_audit_name


class ScheduledAuditMetadata(TypedDict):
    scheduled_audit_name: NotRequired[
        "aws_sdk_iot.types.scheduled_audit_name.ScheduledAuditName"
    ]
    """<p>The name of the scheduled audit.</p>"""
    scheduled_audit_arn: NotRequired[
        "aws_sdk_iot.types.scheduled_audit_arn.ScheduledAuditArn"
    ]
    """<p>The ARN of the scheduled audit.</p>"""
    frequency: NotRequired["aws_sdk_iot.types.audit_frequency.AuditFrequency"]
    """<p>How often the scheduled audit occurs.</p>"""
    day_of_month: NotRequired["aws_sdk_iot.types.day_of_month.DayOfMonth"]
    """<p>The day of the month on which the scheduled audit is run (if the <code>frequency</code> is \"MONTHLY\"). If days 29-31 are specified, and the month does not have that many days, the audit takes place on the \"LAST\" day of the month.</p>"""
    day_of_week: NotRequired["aws_sdk_iot.types.day_of_week.DayOfWeek"]
    """<p>The day of the week on which the scheduled audit is run (if the <code>frequency</code> is \"WEEKLY\" or \"BIWEEKLY\").</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScheduledAuditMetadata) -> dict:
    out: dict = {}
    if "scheduled_audit_name" in value:
        out["scheduledAuditName"] = value["scheduled_audit_name"]
    if "scheduled_audit_arn" in value:
        out["scheduledAuditArn"] = value["scheduled_audit_arn"]
    if "frequency" in value:
        import aws_sdk_iot.types.audit_frequency

        out["frequency"] = aws_sdk_iot.types.audit_frequency.serialize_json(
            value["frequency"]
        )
    if "day_of_month" in value:
        out["dayOfMonth"] = value["day_of_month"]
    if "day_of_week" in value:
        import aws_sdk_iot.types.day_of_week

        out["dayOfWeek"] = aws_sdk_iot.types.day_of_week.serialize_json(
            value["day_of_week"]
        )
    return out


def deserialize_json(data: dict) -> ScheduledAuditMetadata:
    out: ScheduledAuditMetadata = {}  # type: ignore[typeddict-item]
    if "scheduledAuditName" in data:
        out["scheduled_audit_name"] = data["scheduledAuditName"]
    if "scheduledAuditArn" in data:
        out["scheduled_audit_arn"] = data["scheduledAuditArn"]
    if "frequency" in data:
        import aws_sdk_iot.types.audit_frequency

        out["frequency"] = aws_sdk_iot.types.audit_frequency.deserialize_json(
            data["frequency"]
        )
    if "dayOfMonth" in data:
        out["day_of_month"] = data["dayOfMonth"]
    if "dayOfWeek" in data:
        import aws_sdk_iot.types.day_of_week

        out["day_of_week"] = aws_sdk_iot.types.day_of_week.deserialize_json(
            data["dayOfWeek"]
        )
    return out
