"""Generated from Smithy shape ``com.amazonaws.redshift#ClusterSecurityGroupMembership``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.string


class ClusterSecurityGroupMembership(TypedDict, closed=True):
    cluster_security_group_name: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The name of the cluster security group.</p>"""
    status: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The status of the cluster security group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ClusterSecurityGroupMembership, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cluster_security_group_name" in value:
        pairs.append(
            (
                f"{prefix}.ClusterSecurityGroupName",
                str(value["cluster_security_group_name"]),
            )
        )
    if "status" in value:
        pairs.append((f"{prefix}.Status", str(value["status"])))


def deserialize_query(el: Element) -> ClusterSecurityGroupMembership:
    out: ClusterSecurityGroupMembership = {}  # type: ignore[typeddict-item]
    child_cluster_security_group_name = el.find("ClusterSecurityGroupName")
    if child_cluster_security_group_name is not None:
        out["cluster_security_group_name"] = str(
            child_cluster_security_group_name.text or ""
        )
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    return out
