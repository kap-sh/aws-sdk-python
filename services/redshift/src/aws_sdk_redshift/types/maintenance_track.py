"""Generated from Smithy shape ``com.amazonaws.redshift#MaintenanceTrack``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.eligible_tracks_to_update_list
    import aws_sdk_redshift.types.string


class MaintenanceTrack(TypedDict):
    maintenance_track_name: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The name of the maintenance track. Possible values are <code>current</code> and <code>trailing</code>.</p>"""
    database_version: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The version number for the cluster release.</p>"""
    update_targets: NotRequired[
        "aws_sdk_redshift.types.eligible_tracks_to_update_list.EligibleTracksToUpdateList"
    ]
    """<p>An array of <a>UpdateTarget</a> objects to update with the maintenance track. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: MaintenanceTrack, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "maintenance_track_name" in value:
        pairs.append(
            (f"{prefix}.MaintenanceTrackName", str(value["maintenance_track_name"]))
        )
    if "database_version" in value:
        pairs.append((f"{prefix}.DatabaseVersion", str(value["database_version"])))
    if "update_targets" in value:
        import aws_sdk_redshift.types.eligible_tracks_to_update_list

        aws_sdk_redshift.types.eligible_tracks_to_update_list.serialize_query(
            value["update_targets"], pairs, f"{prefix}.UpdateTargets"
        )


def deserialize_query(el: Element) -> MaintenanceTrack:
    out: MaintenanceTrack = {}  # type: ignore[typeddict-item]
    child_maintenance_track_name = el.find("MaintenanceTrackName")
    if child_maintenance_track_name is not None:
        out["maintenance_track_name"] = str(child_maintenance_track_name.text or "")
    child_database_version = el.find("DatabaseVersion")
    if child_database_version is not None:
        out["database_version"] = str(child_database_version.text or "")
    child_update_targets = el.find("UpdateTargets")
    if child_update_targets is not None:
        import aws_sdk_redshift.types.eligible_tracks_to_update_list

        out["update_targets"] = (
            aws_sdk_redshift.types.eligible_tracks_to_update_list.deserialize_query(
                child_update_targets
            )
        )
    return out
