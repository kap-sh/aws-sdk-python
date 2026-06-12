"""Generated from Smithy shape ``com.amazonaws.redshift#CreateScheduledActionMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.boolean_optional
    import aws_sdk_redshift.types.scheduled_action_type
    import aws_sdk_redshift.types.string
    import aws_sdk_redshift.types.t_stamp


class CreateScheduledActionMessage(TypedDict):
    scheduled_action_name: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The name of the scheduled action. The name must be unique within an account. For more information about this parameter, see <a>ScheduledAction</a>. </p>"""
    target_action: NotRequired[
        "aws_sdk_redshift.types.scheduled_action_type.ScheduledActionType"
    ]
    """<p>A JSON format string of the Amazon Redshift API operation with input parameters. For more information about this parameter, see <a>ScheduledAction</a>. </p>"""
    schedule: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The schedule in <code>at( )</code> or <code>cron( )</code> format. For more information about this parameter, see <a>ScheduledAction</a>.</p>"""
    iam_role: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The IAM role to assume to run the target action. For more information about this parameter, see <a>ScheduledAction</a>. </p>"""
    scheduled_action_description: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The description of the scheduled action. </p>"""
    start_time: NotRequired["aws_sdk_redshift.types.t_stamp.TStamp"]
    """<p>The start time in UTC of the scheduled action. Before this time, the scheduled action does not trigger. For more information about this parameter, see <a>ScheduledAction</a>.</p>"""
    end_time: NotRequired["aws_sdk_redshift.types.t_stamp.TStamp"]
    """<p>The end time in UTC of the scheduled action. After this time, the scheduled action does not trigger. For more information about this parameter, see <a>ScheduledAction</a>. </p>"""
    enable: NotRequired["aws_sdk_redshift.types.boolean_optional.BooleanOptional"]
    """<p>If true, the schedule is enabled. If false, the scheduled action does not trigger. For more information about <code>state</code> of the scheduled action, see <a>ScheduledAction</a>. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateScheduledActionMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "scheduled_action_name" in value:
        pairs.append(
            (f"{prefix}.ScheduledActionName", str(value["scheduled_action_name"]))
        )
    if "target_action" in value:
        import aws_sdk_redshift.types.scheduled_action_type

        aws_sdk_redshift.types.scheduled_action_type.serialize_query(
            value["target_action"], pairs, f"{prefix}.TargetAction"
        )
    if "schedule" in value:
        pairs.append((f"{prefix}.Schedule", str(value["schedule"])))
    if "iam_role" in value:
        pairs.append((f"{prefix}.IamRole", str(value["iam_role"])))
    if "scheduled_action_description" in value:
        pairs.append(
            (
                f"{prefix}.ScheduledActionDescription",
                str(value["scheduled_action_description"]),
            )
        )
    if "start_time" in value:
        import aws_sdk_redshift.types.t_stamp

        aws_sdk_redshift.types.t_stamp.serialize_query(
            value["start_time"], pairs, f"{prefix}.StartTime"
        )
    if "end_time" in value:
        import aws_sdk_redshift.types.t_stamp

        aws_sdk_redshift.types.t_stamp.serialize_query(
            value["end_time"], pairs, f"{prefix}.EndTime"
        )
    if "enable" in value:
        pairs.append((f"{prefix}.Enable", "true" if value["enable"] else "false"))


def deserialize_query(el: Element) -> CreateScheduledActionMessage:
    out: CreateScheduledActionMessage = {}  # type: ignore[typeddict-item]
    child_scheduled_action_name = el.find("ScheduledActionName")
    if child_scheduled_action_name is not None:
        out["scheduled_action_name"] = str(child_scheduled_action_name.text or "")
    child_target_action = el.find("TargetAction")
    if child_target_action is not None:
        import aws_sdk_redshift.types.scheduled_action_type

        out["target_action"] = (
            aws_sdk_redshift.types.scheduled_action_type.deserialize_query(
                child_target_action
            )
        )
    child_schedule = el.find("Schedule")
    if child_schedule is not None:
        out["schedule"] = str(child_schedule.text or "")
    child_iam_role = el.find("IamRole")
    if child_iam_role is not None:
        out["iam_role"] = str(child_iam_role.text or "")
    child_scheduled_action_description = el.find("ScheduledActionDescription")
    if child_scheduled_action_description is not None:
        out["scheduled_action_description"] = str(
            child_scheduled_action_description.text or ""
        )
    child_start_time = el.find("StartTime")
    if child_start_time is not None:
        import aws_sdk_redshift.types.t_stamp

        out["start_time"] = aws_sdk_redshift.types.t_stamp.deserialize_query(
            child_start_time
        )
    child_end_time = el.find("EndTime")
    if child_end_time is not None:
        import aws_sdk_redshift.types.t_stamp

        out["end_time"] = aws_sdk_redshift.types.t_stamp.deserialize_query(
            child_end_time
        )
    child_enable = el.find("Enable")
    if child_enable is not None:
        out["enable"] = (child_enable.text or "").lower() == "true"
    return out
