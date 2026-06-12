"""Generated from Smithy shape ``com.amazonaws.redshift#ClusterDbRevisionsList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.cluster_db_revision

ClusterDbRevisionsList: TypeAlias = list[
    "aws_sdk_redshift.types.cluster_db_revision.ClusterDbRevision"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ClusterDbRevisionsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.cluster_db_revision

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.cluster_db_revision.serialize_query(
            item, pairs, f"{prefix}.ClusterDbRevision.{n}"
        )


def deserialize_query(el: Element) -> ClusterDbRevisionsList:
    import aws_sdk_redshift.types.cluster_db_revision

    out: ClusterDbRevisionsList = []
    for child in el.findall("ClusterDbRevision"):
        out.append(aws_sdk_redshift.types.cluster_db_revision.deserialize_query(child))
    return out


def serialize_query_flat(
    value: ClusterDbRevisionsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.cluster_db_revision

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.cluster_db_revision.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ClusterDbRevisionsList:
    import aws_sdk_redshift.types.cluster_db_revision

    out: ClusterDbRevisionsList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_redshift.types.cluster_db_revision.deserialize_query(child))
    return out
