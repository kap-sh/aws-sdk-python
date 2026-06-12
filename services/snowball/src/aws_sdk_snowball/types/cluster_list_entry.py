"""Generated from Smithy shape ``com.amazonaws.snowball#ClusterListEntry``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_snowball.types.cluster_state
    import aws_sdk_snowball.types.string
    import aws_sdk_snowball.types.timestamp


class ClusterListEntry(TypedDict):
    cluster_id: NotRequired["aws_sdk_snowball.types.string.String"]
    """<p>The 39-character ID for the cluster that you want to list, for example <code>CID123e4567-e89b-12d3-a456-426655440000</code>.</p>"""
    cluster_state: NotRequired["aws_sdk_snowball.types.cluster_state.ClusterState"]
    """<p>The current state of this cluster. For information about the state of a specific node, see <a>JobListEntry$JobState</a>.</p>"""
    creation_date: NotRequired["aws_sdk_snowball.types.timestamp.Timestamp"]
    """<p>The creation date for this cluster.</p>"""
    description: NotRequired["aws_sdk_snowball.types.string.String"]
    """<p>Defines an optional description of the cluster, for example <code>Environmental Data Cluster-01</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterListEntry) -> dict:
    out: dict = {}
    if "cluster_id" in value:
        out["ClusterId"] = value["cluster_id"]
    if "cluster_state" in value:
        import aws_sdk_snowball.types.cluster_state

        out["ClusterState"] = (
            aws_sdk_snowball.types.cluster_state.serialize_aws_json_1_1(
                value["cluster_state"]
            )
        )
    if "creation_date" in value:
        import aws_sdk_snowball.types.timestamp

        out["CreationDate"] = aws_sdk_snowball.types.timestamp.serialize_aws_json_1_1(
            value["creation_date"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterListEntry:
    out: ClusterListEntry = {}  # type: ignore[typeddict-item]
    if "ClusterId" in data:
        out["cluster_id"] = data["ClusterId"]
    if "ClusterState" in data:
        import aws_sdk_snowball.types.cluster_state

        out["cluster_state"] = (
            aws_sdk_snowball.types.cluster_state.deserialize_aws_json_1_1(
                data["ClusterState"]
            )
        )
    if "CreationDate" in data:
        import aws_sdk_snowball.types.timestamp

        out["creation_date"] = (
            aws_sdk_snowball.types.timestamp.deserialize_aws_json_1_1(
                data["CreationDate"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    return out
