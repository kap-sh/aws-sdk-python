"""Generated from Smithy shape ``com.amazonaws.neptune#PendingMaintenanceAction``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_neptune.types.string
    import aws_sdk_neptune.types.t_stamp


class PendingMaintenanceAction(TypedDict):
    action: NotRequired["aws_sdk_neptune.types.string.String"]
    """<p>The type of pending maintenance action that is available for the resource.</p>"""
    auto_applied_after_date: NotRequired["aws_sdk_neptune.types.t_stamp.TStamp"]
    """<p>The date of the maintenance window when the action is applied. The maintenance action is applied to the resource during its first maintenance window after this date. If this date is specified, any <code>next-maintenance</code> opt-in requests are ignored.</p>"""
    forced_apply_date: NotRequired["aws_sdk_neptune.types.t_stamp.TStamp"]
    """<p>The date when the maintenance action is automatically applied. The maintenance action is applied to the resource on this date regardless of the maintenance window for the resource. If this date is specified, any <code>immediate</code> opt-in requests are ignored.</p>"""
    opt_in_status: NotRequired["aws_sdk_neptune.types.string.String"]
    """<p>Indicates the type of opt-in request that has been received for the resource.</p>"""
    current_apply_date: NotRequired["aws_sdk_neptune.types.t_stamp.TStamp"]
    """<p>The effective date when the pending maintenance action is applied to the resource. This date takes into account opt-in requests received from the <a>ApplyPendingMaintenanceAction</a> API, the <code>AutoAppliedAfterDate</code>, and the <code>ForcedApplyDate</code>. This value is blank if an opt-in request has not been received and nothing has been specified as <code>AutoAppliedAfterDate</code> or <code>ForcedApplyDate</code>.</p>"""
    description: NotRequired["aws_sdk_neptune.types.string.String"]
    """<p>A description providing more detail about the maintenance action.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PendingMaintenanceAction, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "action" in value:
        pairs.append((f"{prefix}.Action", str(value["action"])))
    if "auto_applied_after_date" in value:
        import aws_sdk_neptune.types.t_stamp

        aws_sdk_neptune.types.t_stamp.serialize_query(
            value["auto_applied_after_date"], pairs, f"{prefix}.AutoAppliedAfterDate"
        )
    if "forced_apply_date" in value:
        import aws_sdk_neptune.types.t_stamp

        aws_sdk_neptune.types.t_stamp.serialize_query(
            value["forced_apply_date"], pairs, f"{prefix}.ForcedApplyDate"
        )
    if "opt_in_status" in value:
        pairs.append((f"{prefix}.OptInStatus", str(value["opt_in_status"])))
    if "current_apply_date" in value:
        import aws_sdk_neptune.types.t_stamp

        aws_sdk_neptune.types.t_stamp.serialize_query(
            value["current_apply_date"], pairs, f"{prefix}.CurrentApplyDate"
        )
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))


def deserialize_query(el: Element) -> PendingMaintenanceAction:
    out: PendingMaintenanceAction = {}  # type: ignore[typeddict-item]
    child_action = el.find("Action")
    if child_action is not None:
        out["action"] = str(child_action.text or "")
    child_auto_applied_after_date = el.find("AutoAppliedAfterDate")
    if child_auto_applied_after_date is not None:
        import aws_sdk_neptune.types.t_stamp

        out["auto_applied_after_date"] = (
            aws_sdk_neptune.types.t_stamp.deserialize_query(
                child_auto_applied_after_date
            )
        )
    child_forced_apply_date = el.find("ForcedApplyDate")
    if child_forced_apply_date is not None:
        import aws_sdk_neptune.types.t_stamp

        out["forced_apply_date"] = aws_sdk_neptune.types.t_stamp.deserialize_query(
            child_forced_apply_date
        )
    child_opt_in_status = el.find("OptInStatus")
    if child_opt_in_status is not None:
        out["opt_in_status"] = str(child_opt_in_status.text or "")
    child_current_apply_date = el.find("CurrentApplyDate")
    if child_current_apply_date is not None:
        import aws_sdk_neptune.types.t_stamp

        out["current_apply_date"] = aws_sdk_neptune.types.t_stamp.deserialize_query(
            child_current_apply_date
        )
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    return out
