"""Generated from Smithy shape ``com.amazonaws.redshift#ClusterDbRevision``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.revision_targets_list
    import aws_sdk_redshift.types.string
    import aws_sdk_redshift.types.t_stamp


class ClusterDbRevision(TypedDict, closed=True):
    cluster_identifier: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The unique identifier of the cluster.</p>"""
    current_database_revision: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>A string representing the current cluster version.</p>"""
    database_revision_release_date: NotRequired["aws_sdk_redshift.types.t_stamp.TStamp"]
    """<p>The date on which the database revision was released.</p>"""
    revision_targets: NotRequired[
        "aws_sdk_redshift.types.revision_targets_list.RevisionTargetsList"
    ]
    """<p>A list of <code>RevisionTarget</code> objects, where each object describes the database revision that a cluster can be updated to.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ClusterDbRevision, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cluster_identifier" in value:
        pairs.append((f"{prefix}.ClusterIdentifier", str(value["cluster_identifier"])))
    if "current_database_revision" in value:
        pairs.append(
            (
                f"{prefix}.CurrentDatabaseRevision",
                str(value["current_database_revision"]),
            )
        )
    if "database_revision_release_date" in value:
        import aws_sdk_redshift.types.t_stamp

        aws_sdk_redshift.types.t_stamp.serialize_query(
            value["database_revision_release_date"],
            pairs,
            f"{prefix}.DatabaseRevisionReleaseDate",
        )
    if "revision_targets" in value:
        import aws_sdk_redshift.types.revision_targets_list

        aws_sdk_redshift.types.revision_targets_list.serialize_query(
            value["revision_targets"], pairs, f"{prefix}.RevisionTargets"
        )


def deserialize_query(el: Element) -> ClusterDbRevision:
    out: ClusterDbRevision = {}  # type: ignore[typeddict-item]
    child_cluster_identifier = el.find("ClusterIdentifier")
    if child_cluster_identifier is not None:
        out["cluster_identifier"] = str(child_cluster_identifier.text or "")
    child_current_database_revision = el.find("CurrentDatabaseRevision")
    if child_current_database_revision is not None:
        out["current_database_revision"] = str(
            child_current_database_revision.text or ""
        )
    child_database_revision_release_date = el.find("DatabaseRevisionReleaseDate")
    if child_database_revision_release_date is not None:
        import aws_sdk_redshift.types.t_stamp

        out["database_revision_release_date"] = (
            aws_sdk_redshift.types.t_stamp.deserialize_query(
                child_database_revision_release_date
            )
        )
    child_revision_targets = el.find("RevisionTargets")
    if child_revision_targets is not None:
        import aws_sdk_redshift.types.revision_targets_list

        out["revision_targets"] = (
            aws_sdk_redshift.types.revision_targets_list.deserialize_query(
                child_revision_targets
            )
        )
    return out
