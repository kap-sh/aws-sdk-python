"""Generated from Smithy shape ``com.amazonaws.redshift#CreateClusterSnapshotMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.integer_optional
    import capo_redshift.types.string
    import capo_redshift.types.tag_list


class CreateClusterSnapshotMessage(TypedDict, closed=True):
    snapshot_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>A unique identifier for the snapshot that you are requesting. This identifier must be unique for all snapshots within the Amazon Web Services account.</p> <p>Constraints:</p> <ul> <li> <p>Cannot be null, empty, or blank</p> </li> <li> <p>Must contain from 1 to 255 alphanumeric characters or hyphens</p> </li> <li> <p>First character must be a letter</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens</p> </li> </ul> <p>Example: <code>my-snapshot-id</code> </p>"""
    cluster_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>The cluster identifier for which you want a snapshot.</p>"""
    manual_snapshot_retention_period: NotRequired[
        "capo_redshift.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of days that a manual snapshot is retained. If the value is -1, the manual snapshot is retained indefinitely. </p> <p>The value must be either -1 or an integer between 1 and 3,653.</p> <p>The default value is -1.</p>"""
    tags: NotRequired["capo_redshift.types.tag_list.TagList"]
    """<p>A list of tag instances.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateClusterSnapshotMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "snapshot_identifier" in value:
        pairs.append(
            (f"{prefix}.SnapshotIdentifier", str(value["snapshot_identifier"]))
        )
    if "cluster_identifier" in value:
        pairs.append((f"{prefix}.ClusterIdentifier", str(value["cluster_identifier"])))
    if "manual_snapshot_retention_period" in value:
        pairs.append(
            (
                f"{prefix}.ManualSnapshotRetentionPeriod",
                str(value["manual_snapshot_retention_period"]),
            )
        )
    if "tags" in value:
        import capo_redshift.types.tag_list

        capo_redshift.types.tag_list.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )


def deserialize_query(el: Element) -> CreateClusterSnapshotMessage:
    out: CreateClusterSnapshotMessage = {}  # type: ignore[typeddict-item]
    child_snapshot_identifier = el.find("SnapshotIdentifier")
    if child_snapshot_identifier is not None:
        out["snapshot_identifier"] = str(child_snapshot_identifier.text or "")
    child_cluster_identifier = el.find("ClusterIdentifier")
    if child_cluster_identifier is not None:
        out["cluster_identifier"] = str(child_cluster_identifier.text or "")
    child_manual_snapshot_retention_period = el.find("ManualSnapshotRetentionPeriod")
    if child_manual_snapshot_retention_period is not None:
        out["manual_snapshot_retention_period"] = int(
            child_manual_snapshot_retention_period.text or ""
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_redshift.types.tag_list

        out["tags"] = capo_redshift.types.tag_list.deserialize_query(child_tags)
    return out
