"""Generated from Smithy shape ``com.amazonaws.redshift#DeleteClusterSecurityGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.string


class DeleteClusterSecurityGroupMessage(TypedDict, closed=True):
    cluster_security_group_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the cluster security group to be deleted.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteClusterSecurityGroupMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cluster_security_group_name" in value:
        pairs.append(
            (
                f"{prefix}.ClusterSecurityGroupName",
                str(value["cluster_security_group_name"]),
            )
        )


def deserialize_query(el: Element) -> DeleteClusterSecurityGroupMessage:
    out: DeleteClusterSecurityGroupMessage = {}  # type: ignore[typeddict-item]
    child_cluster_security_group_name = el.find("ClusterSecurityGroupName")
    if child_cluster_security_group_name is not None:
        out["cluster_security_group_name"] = str(
            child_cluster_security_group_name.text or ""
        )
    return out
