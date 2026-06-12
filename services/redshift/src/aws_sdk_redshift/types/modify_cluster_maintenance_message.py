"""Generated from Smithy shape ``com.amazonaws.redshift#ModifyClusterMaintenanceMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.boolean_optional
    import aws_sdk_redshift.types.integer_optional
    import aws_sdk_redshift.types.string
    import aws_sdk_redshift.types.t_stamp


class ModifyClusterMaintenanceMessage(TypedDict):
    cluster_identifier: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>A unique identifier for the cluster.</p>"""
    defer_maintenance: NotRequired[
        "aws_sdk_redshift.types.boolean_optional.BooleanOptional"
    ]
    """<p>A boolean indicating whether to enable the deferred maintenance window. </p>"""
    defer_maintenance_identifier: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>A unique identifier for the deferred maintenance window.</p>"""
    defer_maintenance_start_time: NotRequired["aws_sdk_redshift.types.t_stamp.TStamp"]
    """<p>A timestamp indicating the start time for the deferred maintenance window.</p>"""
    defer_maintenance_end_time: NotRequired["aws_sdk_redshift.types.t_stamp.TStamp"]
    """<p>A timestamp indicating end time for the deferred maintenance window. If you specify an end time, you can't specify a duration.</p>"""
    defer_maintenance_duration: NotRequired[
        "aws_sdk_redshift.types.integer_optional.IntegerOptional"
    ]
    """<p>An integer indicating the duration of the maintenance window in days. If you specify a duration, you can't specify an end time. The duration must be 60 days or less.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyClusterMaintenanceMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cluster_identifier" in value:
        pairs.append((f"{prefix}.ClusterIdentifier", str(value["cluster_identifier"])))
    if "defer_maintenance" in value:
        pairs.append(
            (
                f"{prefix}.DeferMaintenance",
                "true" if value["defer_maintenance"] else "false",
            )
        )
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
    if "defer_maintenance_duration" in value:
        pairs.append(
            (
                f"{prefix}.DeferMaintenanceDuration",
                str(value["defer_maintenance_duration"]),
            )
        )


def deserialize_query(el: Element) -> ModifyClusterMaintenanceMessage:
    out: ModifyClusterMaintenanceMessage = {}  # type: ignore[typeddict-item]
    child_cluster_identifier = el.find("ClusterIdentifier")
    if child_cluster_identifier is not None:
        out["cluster_identifier"] = str(child_cluster_identifier.text or "")
    child_defer_maintenance = el.find("DeferMaintenance")
    if child_defer_maintenance is not None:
        out["defer_maintenance"] = (
            child_defer_maintenance.text or ""
        ).lower() == "true"
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
    child_defer_maintenance_duration = el.find("DeferMaintenanceDuration")
    if child_defer_maintenance_duration is not None:
        out["defer_maintenance_duration"] = int(
            child_defer_maintenance_duration.text or ""
        )
    return out
