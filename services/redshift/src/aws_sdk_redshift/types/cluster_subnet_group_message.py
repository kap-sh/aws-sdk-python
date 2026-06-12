"""Generated from Smithy shape ``com.amazonaws.redshift#ClusterSubnetGroupMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.cluster_subnet_groups
    import aws_sdk_redshift.types.string


class ClusterSubnetGroupMessage(TypedDict):
    marker: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the <code>Marker</code> parameter and retrying the command. If the <code>Marker</code> field is empty, all response records have been retrieved for the request. </p>"""
    cluster_subnet_groups: NotRequired[
        "aws_sdk_redshift.types.cluster_subnet_groups.ClusterSubnetGroups"
    ]
    """<p>A list of <a>ClusterSubnetGroup</a> instances. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ClusterSubnetGroupMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "cluster_subnet_groups" in value:
        import aws_sdk_redshift.types.cluster_subnet_groups

        aws_sdk_redshift.types.cluster_subnet_groups.serialize_query(
            value["cluster_subnet_groups"], pairs, f"{prefix}.ClusterSubnetGroups"
        )


def deserialize_query(el: Element) -> ClusterSubnetGroupMessage:
    out: ClusterSubnetGroupMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_cluster_subnet_groups = el.find("ClusterSubnetGroups")
    if child_cluster_subnet_groups is not None:
        import aws_sdk_redshift.types.cluster_subnet_groups

        out["cluster_subnet_groups"] = (
            aws_sdk_redshift.types.cluster_subnet_groups.deserialize_query(
                child_cluster_subnet_groups
            )
        )
    return out
