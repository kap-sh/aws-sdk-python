"""Generated from Smithy shape ``com.amazonaws.redshift#ClusterSecurityGroups``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.cluster_security_group

ClusterSecurityGroups: TypeAlias = list[
    "capo_redshift.types.cluster_security_group.ClusterSecurityGroup"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ClusterSecurityGroups, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.cluster_security_group

    for n, item in enumerate(value, 1):
        capo_redshift.types.cluster_security_group.serialize_query(
            item, pairs, f"{prefix}.ClusterSecurityGroup.{n}"
        )


def deserialize_query(el: Element) -> ClusterSecurityGroups:
    import capo_redshift.types.cluster_security_group

    out: ClusterSecurityGroups = []
    for child in el.findall("ClusterSecurityGroup"):
        out.append(capo_redshift.types.cluster_security_group.deserialize_query(child))
    return out


def serialize_query_flat(
    value: ClusterSecurityGroups, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.cluster_security_group

    for n, item in enumerate(value, 1):
        capo_redshift.types.cluster_security_group.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ClusterSecurityGroups:
    import capo_redshift.types.cluster_security_group

    out: ClusterSecurityGroups = []
    for child in parent.findall(tag):
        out.append(capo_redshift.types.cluster_security_group.deserialize_query(child))
    return out
