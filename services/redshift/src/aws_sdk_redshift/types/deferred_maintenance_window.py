"""Generated from Smithy shape ``com.amazonaws.redshift#DeferredMaintenanceWindow``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.string
    import aws_sdk_redshift.types.t_stamp


class DeferredMaintenanceWindow(TypedDict):
    defer_maintenance_identifier: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>A unique identifier for the maintenance window.</p>"""
    defer_maintenance_start_time: NotRequired["aws_sdk_redshift.types.t_stamp.TStamp"]
    """<p> A timestamp for the beginning of the time period when we defer maintenance.</p>"""
    defer_maintenance_end_time: NotRequired["aws_sdk_redshift.types.t_stamp.TStamp"]
    """<p> A timestamp for the end of the time period when we defer maintenance.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeferredMaintenanceWindow, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "defer_maintenance_identifier" in value:
        pairs.append(
            (
                f"{prefix}.DeferMaintenanceIdentifier",
                str(value["defer_maintenance_identifier"]),
            )
        )
    if "defer_maintenance_start_time" in value:
        import aws_sdk_redshift.types.t_stamp

        aws_sdk_redshift.types.t_stamp.serialize_query(
            value["defer_maintenance_start_time"],
            pairs,
            f"{prefix}.DeferMaintenanceStartTime",
        )
    if "defer_maintenance_end_time" in value:
        import aws_sdk_redshift.types.t_stamp

        aws_sdk_redshift.types.t_stamp.serialize_query(
            value["defer_maintenance_end_time"],
            pairs,
            f"{prefix}.DeferMaintenanceEndTime",
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
        import aws_sdk_redshift.types.t_stamp

        out["defer_maintenance_start_time"] = (
            aws_sdk_redshift.types.t_stamp.deserialize_query(
                child_defer_maintenance_start_time
            )
        )
    child_defer_maintenance_end_time = el.find("DeferMaintenanceEndTime")
    if child_defer_maintenance_end_time is not None:
        import aws_sdk_redshift.types.t_stamp

        out["defer_maintenance_end_time"] = (
            aws_sdk_redshift.types.t_stamp.deserialize_query(
                child_defer_maintenance_end_time
            )
        )
    return out
