"""Generated from Smithy shape ``com.amazonaws.redshift#UpdateTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.string
    import aws_sdk_redshift.types.supported_operation_list


class UpdateTarget(TypedDict, closed=True):
    maintenance_track_name: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The name of the new maintenance track.</p>"""
    database_version: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The cluster version for the new maintenance track.</p>"""
    supported_operations: NotRequired[
        "aws_sdk_redshift.types.supported_operation_list.SupportedOperationList"
    ]
    """<p>A list of operations supported by the maintenance track.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateTarget, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "maintenance_track_name" in value:
        pairs.append(
            (f"{prefix}.MaintenanceTrackName", str(value["maintenance_track_name"]))
        )
    if "database_version" in value:
        pairs.append((f"{prefix}.DatabaseVersion", str(value["database_version"])))
    if "supported_operations" in value:
        import aws_sdk_redshift.types.supported_operation_list

        aws_sdk_redshift.types.supported_operation_list.serialize_query(
            value["supported_operations"], pairs, f"{prefix}.SupportedOperations"
        )


def deserialize_query(el: Element) -> UpdateTarget:
    out: UpdateTarget = {}  # type: ignore[typeddict-item]
    child_maintenance_track_name = el.find("MaintenanceTrackName")
    if child_maintenance_track_name is not None:
        out["maintenance_track_name"] = str(child_maintenance_track_name.text or "")
    child_database_version = el.find("DatabaseVersion")
    if child_database_version is not None:
        out["database_version"] = str(child_database_version.text or "")
    child_supported_operations = el.find("SupportedOperations")
    if child_supported_operations is not None:
        import aws_sdk_redshift.types.supported_operation_list

        out["supported_operations"] = (
            aws_sdk_redshift.types.supported_operation_list.deserialize_query(
                child_supported_operations
            )
        )
    return out
