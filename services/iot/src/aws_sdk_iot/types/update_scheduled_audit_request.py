"""Generated from Smithy shape ``com.amazonaws.iot#UpdateScheduledAuditRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.audit_frequency
    import aws_sdk_iot.types.day_of_month
    import aws_sdk_iot.types.day_of_week
    import aws_sdk_iot.types.scheduled_audit_name
    import aws_sdk_iot.types.target_audit_check_names


class UpdateScheduledAuditRequest(TypedDict, closed=True):
    frequency: NotRequired["aws_sdk_iot.types.audit_frequency.AuditFrequency"]
    """<p>How often the scheduled audit takes place, either <code>DAILY</code>, <code>WEEKLY</code>, <code>BIWEEKLY</code>, or <code>MONTHLY</code>. The start time of each audit is determined by the system.</p>"""
    day_of_month: NotRequired["aws_sdk_iot.types.day_of_month.DayOfMonth"]
    r"""<p>The day of the month on which the scheduled audit takes place. This can be <code>1</code> through <code>31</code> or <code>LAST</code>. This field is required if the <code>frequency</code> parameter is set to <code>MONTHLY</code>. If days 29-31 are specified, and the month does not have that many days, the audit takes place on the \"LAST\" day of the month.</p>"""
    day_of_week: NotRequired["aws_sdk_iot.types.day_of_week.DayOfWeek"]
    r"""<p>The day of the week on which the scheduled audit takes place. This can be one of <code>SUN</code>, <code>MON</code>, <code>TUE</code>, <code>WED</code>, <code>THU</code>, <code>FRI</code>, or <code>SAT</code>. This field is required if the \"frequency\" parameter is set to <code>WEEKLY</code> or <code>BIWEEKLY</code>.</p>"""
    target_check_names: NotRequired[
        "aws_sdk_iot.types.target_audit_check_names.TargetAuditCheckNames"
    ]
    """<p>Which checks are performed during the scheduled audit. Checks must be enabled for your account. (Use <code>DescribeAccountAuditConfiguration</code> to see the list of all checks, including those that are enabled or use <code>UpdateAccountAuditConfiguration</code> to select which checks are enabled.)</p>"""
    scheduled_audit_name: "aws_sdk_iot.types.scheduled_audit_name.ScheduledAuditName"
    """<p>The name of the scheduled audit. (Max. 128 chars)</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateScheduledAuditRequest) -> dict:
    out: dict = {}
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
    if "target_check_names" in value:
        import aws_sdk_iot.types.target_audit_check_names

        out["targetCheckNames"] = (
            aws_sdk_iot.types.target_audit_check_names.serialize_json(
                value["target_check_names"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateScheduledAuditRequest:
    out: UpdateScheduledAuditRequest = {}  # type: ignore[typeddict-item]
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
    if "targetCheckNames" in data:
        import aws_sdk_iot.types.target_audit_check_names

        out["target_check_names"] = (
            aws_sdk_iot.types.target_audit_check_names.deserialize_json(
                data["targetCheckNames"]
            )
        )
    return out
