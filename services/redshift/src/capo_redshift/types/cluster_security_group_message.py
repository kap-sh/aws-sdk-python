"""Generated from Smithy shape ``com.amazonaws.redshift#ClusterSecurityGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.cluster_security_groups
    import capo_redshift.types.string


class ClusterSecurityGroupMessage(TypedDict, closed=True):
    marker: NotRequired["capo_redshift.types.string.String"]
    """<p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the <code>Marker</code> parameter and retrying the command. If the <code>Marker</code> field is empty, all response records have been retrieved for the request. </p>"""
    cluster_security_groups: NotRequired[
        "capo_redshift.types.cluster_security_groups.ClusterSecurityGroups"
    ]
    """<p>A list of <a>ClusterSecurityGroup</a> instances. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ClusterSecurityGroupMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "cluster_security_groups" in value:
        import capo_redshift.types.cluster_security_groups

        capo_redshift.types.cluster_security_groups.serialize_query(
            value["cluster_security_groups"], pairs, f"{prefix}.ClusterSecurityGroups"
        )


def deserialize_query(el: Element) -> ClusterSecurityGroupMessage:
    out: ClusterSecurityGroupMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_cluster_security_groups = el.find("ClusterSecurityGroups")
    if child_cluster_security_groups is not None:
        import capo_redshift.types.cluster_security_groups

        out["cluster_security_groups"] = (
            capo_redshift.types.cluster_security_groups.deserialize_query(
                child_cluster_security_groups
            )
        )
    return out
