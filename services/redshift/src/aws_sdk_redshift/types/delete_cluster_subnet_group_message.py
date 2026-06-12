"""Generated from Smithy shape ``com.amazonaws.redshift#DeleteClusterSubnetGroupMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.string


class DeleteClusterSubnetGroupMessage(TypedDict):
    cluster_subnet_group_name: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The name of the cluster subnet group name to be deleted.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteClusterSubnetGroupMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cluster_subnet_group_name" in value:
        pairs.append(
            (
                f"{prefix}.ClusterSubnetGroupName",
                str(value["cluster_subnet_group_name"]),
            )
        )


def deserialize_query(el: Element) -> DeleteClusterSubnetGroupMessage:
    out: DeleteClusterSubnetGroupMessage = {}  # type: ignore[typeddict-item]
    child_cluster_subnet_group_name = el.find("ClusterSubnetGroupName")
    if child_cluster_subnet_group_name is not None:
        out["cluster_subnet_group_name"] = str(
            child_cluster_subnet_group_name.text or ""
        )
    return out
