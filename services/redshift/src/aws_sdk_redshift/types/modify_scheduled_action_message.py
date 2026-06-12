"""Generated from Smithy shape ``com.amazonaws.redshift#ModifyScheduledActionMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.boolean_optional
    import aws_sdk_redshift.types.scheduled_action_type
    import aws_sdk_redshift.types.string
    import aws_sdk_redshift.types.t_stamp


class ModifyScheduledActionMessage(TypedDict):
    scheduled_action_name: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The name of the scheduled action to modify. </p>"""
    target_action: NotRequired[
        "aws_sdk_redshift.types.scheduled_action_type.ScheduledActionType"
    ]
    """<p>A modified JSON format of the scheduled action. For more information about this parameter, see <a>ScheduledAction</a>. </p>"""
    schedule: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>A modified schedule in either <code>at( )</code> or <code>cron( )</code> format. For more information about this parameter, see <a>ScheduledAction</a>.</p>"""
    iam_role: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>A different IAM role to assume to run the target action. For more information about this parameter, see <a>ScheduledAction</a>.</p>"""
    scheduled_action_description: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>A modified description of the scheduled action. </p>"""
    start_time: NotRequired["aws_sdk_redshift.types.t_stamp.TStamp"]
    """<p>A modified start time of the scheduled action. For more information about this parameter, see <a>ScheduledAction</a>. </p>"""
    end_time: NotRequired["aws_sdk_redshift.types.t_stamp.TStamp"]
    """<p>A modified end time of the scheduled action. For more information about this parameter, see <a>ScheduledAction</a>. </p>"""
    enable: NotRequired["aws_sdk_redshift.types.boolean_optional.BooleanOptional"]
    """<p>A modified enable flag of the scheduled action. If true, the scheduled action is active. If false, the scheduled action is disabled. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyScheduledActionMessage, pairs: list[tuple[str, str]], prefix: str
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


def deserialize_query(el: Element) -> ModifyScheduledActionMessage:
    out: ModifyScheduledActionMessage = {}  # type: ignore[typeddict-item]
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
