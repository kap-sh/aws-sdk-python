"""Generated from Smithy shape ``com.amazonaws.autoscaling#InstanceRefresh``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.desired_configuration
    import capo_auto_scaling.types.instance_refresh_progress_details
    import capo_auto_scaling.types.instance_refresh_status
    import capo_auto_scaling.types.instances_to_update
    import capo_auto_scaling.types.int_percent
    import capo_auto_scaling.types.refresh_preferences
    import capo_auto_scaling.types.refresh_strategy
    import capo_auto_scaling.types.rollback_details
    import capo_auto_scaling.types.timestamp_type
    import capo_auto_scaling.types.xml_string_max_len255
    import capo_auto_scaling.types.xml_string_max_len1023


class InstanceRefresh(TypedDict, closed=True):
    instance_refresh_id: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The instance refresh ID.</p>"""
    auto_scaling_group_name: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the Auto Scaling group.</p>"""
    status: NotRequired[
        "capo_auto_scaling.types.instance_refresh_status.InstanceRefreshStatus"
    ]
    """<p>The current status for the instance refresh operation:</p> <ul> <li> <p> <code>Pending</code> - The request was created, but the instance refresh has not started.</p> </li> <li> <p> <code>InProgress</code> - An instance refresh is in progress.</p> </li> <li> <p> <code>Successful</code> - An instance refresh completed successfully.</p> </li> <li> <p> <code>Failed</code> - An instance refresh failed to complete. You can troubleshoot using the status reason and the scaling activities. </p> </li> <li> <p> <code>Cancelling</code> - An ongoing instance refresh is being cancelled.</p> </li> <li> <p> <code>Cancelled</code> - The instance refresh is cancelled. </p> </li> <li> <p> <code>RollbackInProgress</code> - An instance refresh is being rolled back.</p> </li> <li> <p> <code>RollbackFailed</code> - The rollback failed to complete. You can troubleshoot using the status reason and the scaling activities.</p> </li> <li> <p> <code>RollbackSuccessful</code> - The rollback completed successfully.</p> </li> <li> <p> <code>Baking</code> - Waiting the specified bake time after an instance refresh has finished updating instances.</p> </li> </ul>"""
    status_reason: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len1023.XmlStringMaxLen1023"
    ]
    """<p>The explanation for the specific status assigned to this operation.</p>"""
    start_time: NotRequired["capo_auto_scaling.types.timestamp_type.TimestampType"]
    """<p>The date and time at which the instance refresh began.</p>"""
    end_time: NotRequired["capo_auto_scaling.types.timestamp_type.TimestampType"]
    """<p>The date and time at which the instance refresh ended.</p>"""
    percentage_complete: NotRequired["capo_auto_scaling.types.int_percent.IntPercent"]
    """<p>The percentage of the instance refresh that is complete. For each instance replacement, Amazon EC2 Auto Scaling tracks the instance's health status and warm-up time. When the instance's health status changes to healthy and the specified warm-up time passes, the instance is considered updated and is added to the percentage complete.</p> <note> <p> <code>PercentageComplete</code> does not include instances that are replaced during a rollback. This value gradually goes back down to zero during a rollback.</p> </note>"""
    instances_to_update: NotRequired[
        "capo_auto_scaling.types.instances_to_update.InstancesToUpdate"
    ]
    """<p>The number of instances remaining to update before the instance refresh is complete.</p> <note> <p>If you roll back the instance refresh, <code>InstancesToUpdate</code> shows you the number of instances that were not yet updated by the instance refresh. Therefore, these instances don't need to be replaced as part of the rollback.</p> </note>"""
    progress_details: NotRequired[
        "capo_auto_scaling.types.instance_refresh_progress_details.InstanceRefreshProgressDetails"
    ]
    """<p>Additional progress details for an Auto Scaling group that has a warm pool.</p>"""
    preferences: NotRequired[
        "capo_auto_scaling.types.refresh_preferences.RefreshPreferences"
    ]
    """<p>The preferences for an instance refresh.</p>"""
    desired_configuration: NotRequired[
        "capo_auto_scaling.types.desired_configuration.DesiredConfiguration"
    ]
    """<p>Describes the desired configuration for the instance refresh.</p>"""
    rollback_details: NotRequired[
        "capo_auto_scaling.types.rollback_details.RollbackDetails"
    ]
    """<p>The rollback details.</p>"""
    strategy: NotRequired["capo_auto_scaling.types.refresh_strategy.RefreshStrategy"]
    """<p> The strategy to use for the instance refresh. This determines how instances in the Auto Scaling group are updated. Default is Rolling. </p> <ul> <li> <p> <code>Rolling</code> – Terminates instances and launches replacements in batches</p> </li> <li> <p> <code>ReplaceRootVolume</code> – Updates instances by replacing only the root volume without terminating the instance</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: InstanceRefresh, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "instance_refresh_id" in value:
        pairs.append((f"{prefix}.InstanceRefreshId", str(value["instance_refresh_id"])))
    if "auto_scaling_group_name" in value:
        pairs.append(
            (f"{prefix}.AutoScalingGroupName", str(value["auto_scaling_group_name"]))
        )
    if "status" in value:
        import capo_auto_scaling.types.instance_refresh_status

        capo_auto_scaling.types.instance_refresh_status.serialize_query(
            value["status"], pairs, f"{prefix}.Status"
        )
    if "status_reason" in value:
        pairs.append((f"{prefix}.StatusReason", str(value["status_reason"])))
    if "start_time" in value:
        import capo_auto_scaling.types.timestamp_type

        capo_auto_scaling.types.timestamp_type.serialize_query(
            value["start_time"], pairs, f"{prefix}.StartTime"
        )
    if "end_time" in value:
        import capo_auto_scaling.types.timestamp_type

        capo_auto_scaling.types.timestamp_type.serialize_query(
            value["end_time"], pairs, f"{prefix}.EndTime"
        )
    if "percentage_complete" in value:
        pairs.append(
            (f"{prefix}.PercentageComplete", str(value["percentage_complete"]))
        )
    if "instances_to_update" in value:
        pairs.append((f"{prefix}.InstancesToUpdate", str(value["instances_to_update"])))
    if "progress_details" in value:
        import capo_auto_scaling.types.instance_refresh_progress_details

        capo_auto_scaling.types.instance_refresh_progress_details.serialize_query(
            value["progress_details"], pairs, f"{prefix}.ProgressDetails"
        )
    if "preferences" in value:
        import capo_auto_scaling.types.refresh_preferences

        capo_auto_scaling.types.refresh_preferences.serialize_query(
            value["preferences"], pairs, f"{prefix}.Preferences"
        )
    if "desired_configuration" in value:
        import capo_auto_scaling.types.desired_configuration

        capo_auto_scaling.types.desired_configuration.serialize_query(
            value["desired_configuration"], pairs, f"{prefix}.DesiredConfiguration"
        )
    if "rollback_details" in value:
        import capo_auto_scaling.types.rollback_details

        capo_auto_scaling.types.rollback_details.serialize_query(
            value["rollback_details"], pairs, f"{prefix}.RollbackDetails"
        )
    if "strategy" in value:
        import capo_auto_scaling.types.refresh_strategy

        capo_auto_scaling.types.refresh_strategy.serialize_query(
            value["strategy"], pairs, f"{prefix}.Strategy"
        )


def deserialize_query(el: Element) -> InstanceRefresh:
    out: InstanceRefresh = {}  # type: ignore[typeddict-item]
    child_instance_refresh_id = el.find("InstanceRefreshId")
    if child_instance_refresh_id is not None:
        out["instance_refresh_id"] = str(child_instance_refresh_id.text or "")
    child_auto_scaling_group_name = el.find("AutoScalingGroupName")
    if child_auto_scaling_group_name is not None:
        out["auto_scaling_group_name"] = str(child_auto_scaling_group_name.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        import capo_auto_scaling.types.instance_refresh_status

        out["status"] = (
            capo_auto_scaling.types.instance_refresh_status.deserialize_query(
                child_status
            )
        )
    child_status_reason = el.find("StatusReason")
    if child_status_reason is not None:
        out["status_reason"] = str(child_status_reason.text or "")
    child_start_time = el.find("StartTime")
    if child_start_time is not None:
        import capo_auto_scaling.types.timestamp_type

        out["start_time"] = capo_auto_scaling.types.timestamp_type.deserialize_query(
            child_start_time
        )
    child_end_time = el.find("EndTime")
    if child_end_time is not None:
        import capo_auto_scaling.types.timestamp_type

        out["end_time"] = capo_auto_scaling.types.timestamp_type.deserialize_query(
            child_end_time
        )
    child_percentage_complete = el.find("PercentageComplete")
    if child_percentage_complete is not None:
        out["percentage_complete"] = int(child_percentage_complete.text or "")
    child_instances_to_update = el.find("InstancesToUpdate")
    if child_instances_to_update is not None:
        out["instances_to_update"] = int(child_instances_to_update.text or "")
    child_progress_details = el.find("ProgressDetails")
    if child_progress_details is not None:
        import capo_auto_scaling.types.instance_refresh_progress_details

        out["progress_details"] = (
            capo_auto_scaling.types.instance_refresh_progress_details.deserialize_query(
                child_progress_details
            )
        )
    child_preferences = el.find("Preferences")
    if child_preferences is not None:
        import capo_auto_scaling.types.refresh_preferences

        out["preferences"] = (
            capo_auto_scaling.types.refresh_preferences.deserialize_query(
                child_preferences
            )
        )
    child_desired_configuration = el.find("DesiredConfiguration")
    if child_desired_configuration is not None:
        import capo_auto_scaling.types.desired_configuration

        out["desired_configuration"] = (
            capo_auto_scaling.types.desired_configuration.deserialize_query(
                child_desired_configuration
            )
        )
    child_rollback_details = el.find("RollbackDetails")
    if child_rollback_details is not None:
        import capo_auto_scaling.types.rollback_details

        out["rollback_details"] = (
            capo_auto_scaling.types.rollback_details.deserialize_query(
                child_rollback_details
            )
        )
    child_strategy = el.find("Strategy")
    if child_strategy is not None:
        import capo_auto_scaling.types.refresh_strategy

        out["strategy"] = capo_auto_scaling.types.refresh_strategy.deserialize_query(
            child_strategy
        )
    return out
