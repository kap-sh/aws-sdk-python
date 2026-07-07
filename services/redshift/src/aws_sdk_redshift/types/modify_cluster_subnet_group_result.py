"""Generated from Smithy shape ``com.amazonaws.redshift#ModifyClusterSubnetGroupResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.cluster_subnet_group


class ModifyClusterSubnetGroupResult(TypedDict, closed=True):
    cluster_subnet_group: NotRequired[
        "aws_sdk_redshift.types.cluster_subnet_group.ClusterSubnetGroup"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyClusterSubnetGroupResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cluster_subnet_group" in value:
        import aws_sdk_redshift.types.cluster_subnet_group

        aws_sdk_redshift.types.cluster_subnet_group.serialize_query(
            value["cluster_subnet_group"], pairs, f"{prefix}.ClusterSubnetGroup"
        )


def deserialize_query(el: Element) -> ModifyClusterSubnetGroupResult:
    out: ModifyClusterSubnetGroupResult = {}  # type: ignore[typeddict-item]
    child_cluster_subnet_group = el.find("ClusterSubnetGroup")
    if child_cluster_subnet_group is not None:
        import aws_sdk_redshift.types.cluster_subnet_group

        out["cluster_subnet_group"] = (
            aws_sdk_redshift.types.cluster_subnet_group.deserialize_query(
                child_cluster_subnet_group
            )
        )
    return out
