"""Generated from Smithy shape ``com.amazonaws.redshift#CreateClusterSecurityGroupResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.cluster_security_group


class CreateClusterSecurityGroupResult(TypedDict, closed=True):
    cluster_security_group: NotRequired[
        "capo_redshift.types.cluster_security_group.ClusterSecurityGroup"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateClusterSecurityGroupResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cluster_security_group" in value:
        import capo_redshift.types.cluster_security_group

        capo_redshift.types.cluster_security_group.serialize_query(
            value["cluster_security_group"], pairs, f"{prefix}.ClusterSecurityGroup"
        )


def deserialize_query(el: Element) -> CreateClusterSecurityGroupResult:
    out: CreateClusterSecurityGroupResult = {}  # type: ignore[typeddict-item]
    child_cluster_security_group = el.find("ClusterSecurityGroup")
    if child_cluster_security_group is not None:
        import capo_redshift.types.cluster_security_group

        out["cluster_security_group"] = (
            capo_redshift.types.cluster_security_group.deserialize_query(
                child_cluster_security_group
            )
        )
    return out
