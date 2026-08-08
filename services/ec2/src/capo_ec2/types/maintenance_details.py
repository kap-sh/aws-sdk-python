"""Generated from Smithy shape ``com.amazonaws.ec2#MaintenanceDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.string


class MaintenanceDetails(TypedDict, closed=True):
    pending_maintenance: NotRequired["capo_ec2.types.string.String"]
    """<p>Verify existence of a pending maintenance.</p>"""
    maintenance_auto_applied_after: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The timestamp after which Amazon Web Services will automatically apply maintenance.</p>"""
    last_maintenance_applied: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>Timestamp of last applied maintenance.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: MaintenanceDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "pending_maintenance" in value:
        pairs.append(
            (f"{key_prefix}PendingMaintenance", str(value["pending_maintenance"]))
        )
    if "maintenance_auto_applied_after" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["maintenance_auto_applied_after"],
            pairs,
            f"{key_prefix}MaintenanceAutoAppliedAfter",
        )
    if "last_maintenance_applied" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["last_maintenance_applied"],
            pairs,
            f"{key_prefix}LastMaintenanceApplied",
        )


def deserialize_ec2_query(el: Element) -> MaintenanceDetails:
    out: MaintenanceDetails = {}  # type: ignore[typeddict-item]
    child_pending_maintenance = el.find("pendingMaintenance")
    if child_pending_maintenance is not None:
        out["pending_maintenance"] = str(child_pending_maintenance.text or "")
    child_maintenance_auto_applied_after = el.find("maintenanceAutoAppliedAfter")
    if child_maintenance_auto_applied_after is not None:
        import capo_ec2.types.millisecond_date_time

        out["maintenance_auto_applied_after"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_maintenance_auto_applied_after
            )
        )
    child_last_maintenance_applied = el.find("lastMaintenanceApplied")
    if child_last_maintenance_applied is not None:
        import capo_ec2.types.millisecond_date_time

        out["last_maintenance_applied"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_last_maintenance_applied
            )
        )
    return out
