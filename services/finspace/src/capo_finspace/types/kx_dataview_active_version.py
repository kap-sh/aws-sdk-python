"""Generated from Smithy shape ``com.amazonaws.finspace#KxDataviewActiveVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace.types.attached_cluster_list
    import capo_finspace.types.changeset_id
    import capo_finspace.types.kx_dataview_segment_configuration_list
    import capo_finspace.types.timestamp
    import capo_finspace.types.version_id


class KxDataviewActiveVersion(TypedDict, closed=True):
    changeset_id: NotRequired["capo_finspace.types.changeset_id.ChangesetId"]
    """<p>A unique identifier for the changeset.</p>"""
    segment_configurations: NotRequired[
        "capo_finspace.types.kx_dataview_segment_configuration_list.KxDataviewSegmentConfigurationList"
    ]
    """<p> The configuration that contains the database path of the data that you want to place on each selected volume. Each segment must have a unique database path for each volume. If you do not explicitly specify any database path for a volume, they are accessible from the cluster through the default S3/object store segment. </p>"""
    attached_clusters: NotRequired[
        "capo_finspace.types.attached_cluster_list.AttachedClusterList"
    ]
    """<p> The list of clusters that are currently using this dataview. </p>"""
    created_timestamp: NotRequired["capo_finspace.types.timestamp.Timestamp"]
    """<p> The timestamp at which the dataview version was active. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.</p>"""
    version_id: NotRequired["capo_finspace.types.version_id.VersionId"]
    """<p> A unique identifier of the active version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KxDataviewActiveVersion) -> dict:
    out: dict = {}
    if "changeset_id" in value:
        out["changesetId"] = value["changeset_id"]
    if "segment_configurations" in value:
        import capo_finspace.types.kx_dataview_segment_configuration_list

        out["segmentConfigurations"] = (
            capo_finspace.types.kx_dataview_segment_configuration_list.serialize_json(
                value["segment_configurations"]
            )
        )
    if "attached_clusters" in value:
        import capo_finspace.types.attached_cluster_list

        out["attachedClusters"] = (
            capo_finspace.types.attached_cluster_list.serialize_json(
                value["attached_clusters"]
            )
        )
    if "created_timestamp" in value:
        import capo_finspace.types.timestamp

        out["createdTimestamp"] = capo_finspace.types.timestamp.serialize_json(
            value["created_timestamp"]
        )
    if "version_id" in value:
        out["versionId"] = value["version_id"]
    return out


def deserialize_json(data: dict) -> KxDataviewActiveVersion:
    out: KxDataviewActiveVersion = {}  # type: ignore[typeddict-item]
    if "changesetId" in data:
        out["changeset_id"] = data["changesetId"]
    if "segmentConfigurations" in data:
        import capo_finspace.types.kx_dataview_segment_configuration_list

        out["segment_configurations"] = (
            capo_finspace.types.kx_dataview_segment_configuration_list.deserialize_json(
                data["segmentConfigurations"]
            )
        )
    if "attachedClusters" in data:
        import capo_finspace.types.attached_cluster_list

        out["attached_clusters"] = (
            capo_finspace.types.attached_cluster_list.deserialize_json(
                data["attachedClusters"]
            )
        )
    if "createdTimestamp" in data:
        import capo_finspace.types.timestamp

        out["created_timestamp"] = capo_finspace.types.timestamp.deserialize_json(
            data["createdTimestamp"]
        )
    if "versionId" in data:
        out["version_id"] = data["versionId"]
    return out
