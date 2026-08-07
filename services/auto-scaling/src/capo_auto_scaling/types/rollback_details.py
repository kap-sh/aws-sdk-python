"""Generated from Smithy shape ``com.amazonaws.autoscaling#RollbackDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.instance_refresh_progress_details
    import capo_auto_scaling.types.instances_to_update
    import capo_auto_scaling.types.int_percent
    import capo_auto_scaling.types.timestamp_type
    import capo_auto_scaling.types.xml_string_max_len1023


class RollbackDetails(TypedDict, closed=True):
    rollback_reason: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len1023.XmlStringMaxLen1023"
    ]
    """<p>The reason for this instance refresh rollback (for example, whether a manual or automatic rollback was initiated).</p>"""
    rollback_start_time: NotRequired[
        "capo_auto_scaling.types.timestamp_type.TimestampType"
    ]
    """<p>The date and time at which the rollback began.</p>"""
    percentage_complete_on_rollback: NotRequired[
        "capo_auto_scaling.types.int_percent.IntPercent"
    ]
    """<p>Indicates the value of <code>PercentageComplete</code> at the time the rollback started.</p>"""
    instances_to_update_on_rollback: NotRequired[
        "capo_auto_scaling.types.instances_to_update.InstancesToUpdate"
    ]
    """<p>Indicates the value of <code>InstancesToUpdate</code> at the time the rollback started.</p>"""
    progress_details_on_rollback: NotRequired[
        "capo_auto_scaling.types.instance_refresh_progress_details.InstanceRefreshProgressDetails"
    ]
    """<p>Reports progress on replacing instances in an Auto Scaling group that has a warm pool. This includes separate details for instances in the warm pool and instances in the Auto Scaling group (the live pool).</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RollbackDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "rollback_reason" in value:
        pairs.append((f"{key_prefix}RollbackReason", str(value["rollback_reason"])))
    if "rollback_start_time" in value:
        import capo_auto_scaling.types.timestamp_type

        capo_auto_scaling.types.timestamp_type.serialize_query(
            value["rollback_start_time"], pairs, f"{key_prefix}RollbackStartTime"
        )
    if "percentage_complete_on_rollback" in value:
        pairs.append(
            (
                f"{key_prefix}PercentageCompleteOnRollback",
                str(value["percentage_complete_on_rollback"]),
            )
        )
    if "instances_to_update_on_rollback" in value:
        pairs.append(
            (
                f"{key_prefix}InstancesToUpdateOnRollback",
                str(value["instances_to_update_on_rollback"]),
            )
        )
    if "progress_details_on_rollback" in value:
        import capo_auto_scaling.types.instance_refresh_progress_details

        capo_auto_scaling.types.instance_refresh_progress_details.serialize_query(
            value["progress_details_on_rollback"],
            pairs,
            f"{key_prefix}ProgressDetailsOnRollback",
        )


def deserialize_query(el: Element) -> RollbackDetails:
    out: RollbackDetails = {}  # type: ignore[typeddict-item]
    child_rollback_reason = el.find("RollbackReason")
    if child_rollback_reason is not None:
        out["rollback_reason"] = str(child_rollback_reason.text or "")
    child_rollback_start_time = el.find("RollbackStartTime")
    if child_rollback_start_time is not None:
        import capo_auto_scaling.types.timestamp_type

        out["rollback_start_time"] = (
            capo_auto_scaling.types.timestamp_type.deserialize_query(
                child_rollback_start_time
            )
        )
    child_percentage_complete_on_rollback = el.find("PercentageCompleteOnRollback")
    if child_percentage_complete_on_rollback is not None:
        out["percentage_complete_on_rollback"] = int(
            child_percentage_complete_on_rollback.text or ""
        )
    child_instances_to_update_on_rollback = el.find("InstancesToUpdateOnRollback")
    if child_instances_to_update_on_rollback is not None:
        out["instances_to_update_on_rollback"] = int(
            child_instances_to_update_on_rollback.text or ""
        )
    child_progress_details_on_rollback = el.find("ProgressDetailsOnRollback")
    if child_progress_details_on_rollback is not None:
        import capo_auto_scaling.types.instance_refresh_progress_details

        out["progress_details_on_rollback"] = (
            capo_auto_scaling.types.instance_refresh_progress_details.deserialize_query(
                child_progress_details_on_rollback
            )
        )
    return out
