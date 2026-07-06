"""Generated from Smithy shape ``com.amazonaws.redshift#RevisionTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.string
    import aws_sdk_redshift.types.t_stamp


class RevisionTarget(TypedDict, closed=True):
    database_revision: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>A unique string that identifies the version to update the cluster to. You can use this value in <a>ModifyClusterDbRevision</a>.</p>"""
    description: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>A string that describes the changes and features that will be applied to the cluster when it is updated to the corresponding <a>ClusterDbRevision</a>.</p>"""
    database_revision_release_date: NotRequired["aws_sdk_redshift.types.t_stamp.TStamp"]
    """<p>The date on which the database revision was released.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RevisionTarget, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "database_revision" in value:
        pairs.append((f"{prefix}.DatabaseRevision", str(value["database_revision"])))
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "database_revision_release_date" in value:
        import aws_sdk_redshift.types.t_stamp

        aws_sdk_redshift.types.t_stamp.serialize_query(
            value["database_revision_release_date"],
            pairs,
            f"{prefix}.DatabaseRevisionReleaseDate",
        )


def deserialize_query(el: Element) -> RevisionTarget:
    out: RevisionTarget = {}  # type: ignore[typeddict-item]
    child_database_revision = el.find("DatabaseRevision")
    if child_database_revision is not None:
        out["database_revision"] = str(child_database_revision.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_database_revision_release_date = el.find("DatabaseRevisionReleaseDate")
    if child_database_revision_release_date is not None:
        import aws_sdk_redshift.types.t_stamp

        out["database_revision_release_date"] = (
            aws_sdk_redshift.types.t_stamp.deserialize_query(
                child_database_revision_release_date
            )
        )
    return out
