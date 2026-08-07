"""Generated from Smithy shape ``com.amazonaws.redshift#DeferredMaintenanceWindow``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.string
    import capo_redshift.types.t_stamp


class DeferredMaintenanceWindow(TypedDict, closed=True):
    defer_maintenance_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>A unique identifier for the maintenance window.</p>"""
    defer_maintenance_start_time: NotRequired["capo_redshift.types.t_stamp.TStamp"]
    """<p> A timestamp for the beginning of the time period when we defer maintenance.</p>"""
    defer_maintenance_end_time: NotRequired["capo_redshift.types.t_stamp.TStamp"]
    """<p> A timestamp for the end of the time period when we defer maintenance.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeferredMaintenanceWindow, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "defer_maintenance_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}DeferMaintenanceIdentifier",
                str(value["defer_maintenance_identifier"]),
            )
        )
    if "defer_maintenance_start_time" in value:
        import capo_redshift.types.t_stamp

        capo_redshift.types.t_stamp.serialize_query(
            value["defer_maintenance_start_time"],
            pairs,
            f"{key_prefix}DeferMaintenanceStartTime",
        )
    if "defer_maintenance_end_time" in value:
        import capo_redshift.types.t_stamp

        capo_redshift.types.t_stamp.serialize_query(
            value["defer_maintenance_end_time"],
            pairs,
            f"{key_prefix}DeferMaintenanceEndTime",
        )


def deserialize_query(el: Element) -> DeferredMaintenanceWindow:
    out: DeferredMaintenanceWindow = {}  # type: ignore[typeddict-item]
    child_defer_maintenance_identifier = el.find("DeferMaintenanceIdentifier")
    if child_defer_maintenance_identifier is not None:
        out["defer_maintenance_identifier"] = str(
            child_defer_maintenance_identifier.text or ""
        )
    child_defer_maintenance_start_time = el.find("DeferMaintenanceStartTime")
    if child_defer_maintenance_start_time is not None:
        import capo_redshift.types.t_stamp

        out["defer_maintenance_start_time"] = (
            capo_redshift.types.t_stamp.deserialize_query(
                child_defer_maintenance_start_time
            )
        )
    child_defer_maintenance_end_time = el.find("DeferMaintenanceEndTime")
    if child_defer_maintenance_end_time is not None:
        import capo_redshift.types.t_stamp

        out["defer_maintenance_end_time"] = (
            capo_redshift.types.t_stamp.deserialize_query(
                child_defer_maintenance_end_time
            )
        )
    return out
