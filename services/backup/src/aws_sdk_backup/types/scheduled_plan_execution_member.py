"""Generated from Smithy shape ``com.amazonaws.backup#ScheduledPlanExecutionMember``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup.types.rule_execution_type
    import aws_sdk_backup.types.string
    import aws_sdk_backup.types.timestamp


class ScheduledPlanExecutionMember(TypedDict):
    execution_time: NotRequired["aws_sdk_backup.types.timestamp.timestamp"]
    """<p>The timestamp when the backup is scheduled to run, in Unix format and Coordinated Universal Time (UTC). The value is accurate to milliseconds.</p>"""
    rule_id: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>The unique identifier of the backup rule that will execute at the scheduled time.</p>"""
    rule_execution_type: NotRequired[
        "aws_sdk_backup.types.rule_execution_type.RuleExecutionType"
    ]
    """<p>The type of backup rule execution. Valid values are <code>CONTINUOUS</code> (point-in-time recovery), <code>SNAPSHOTS</code> (snapshot backups), or <code>CONTINUOUS_AND_SNAPSHOTS</code> (both types combined).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScheduledPlanExecutionMember) -> dict:
    out: dict = {}
    if "execution_time" in value:
        import aws_sdk_backup.types.timestamp

        out["ExecutionTime"] = aws_sdk_backup.types.timestamp.serialize_json(
            value["execution_time"]
        )
    if "rule_id" in value:
        out["RuleId"] = value["rule_id"]
    if "rule_execution_type" in value:
        import aws_sdk_backup.types.rule_execution_type

        out["RuleExecutionType"] = (
            aws_sdk_backup.types.rule_execution_type.serialize_json(
                value["rule_execution_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> ScheduledPlanExecutionMember:
    out: ScheduledPlanExecutionMember = {}  # type: ignore[typeddict-item]
    if "ExecutionTime" in data:
        import aws_sdk_backup.types.timestamp

        out["execution_time"] = aws_sdk_backup.types.timestamp.deserialize_json(
            data["ExecutionTime"]
        )
    if "RuleId" in data:
        out["rule_id"] = data["RuleId"]
    if "RuleExecutionType" in data:
        import aws_sdk_backup.types.rule_execution_type

        out["rule_execution_type"] = (
            aws_sdk_backup.types.rule_execution_type.deserialize_json(
                data["RuleExecutionType"]
            )
        )
    return out
