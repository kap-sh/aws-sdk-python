"""Generated from Smithy shape ``com.amazonaws.redshift#ClusterNodesList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.cluster_node

ClusterNodesList: TypeAlias = list["capo_redshift.types.cluster_node.ClusterNode"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ClusterNodesList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.cluster_node

    for n, item in enumerate(value, 1):
        capo_redshift.types.cluster_node.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ClusterNodesList:
    import capo_redshift.types.cluster_node

    out: ClusterNodesList = []
    for child in el.findall("member"):
        out.append(capo_redshift.types.cluster_node.deserialize_query(child))
    return out


def serialize_query_flat(
    value: ClusterNodesList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.cluster_node

    for n, item in enumerate(value, 1):
        capo_redshift.types.cluster_node.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> ClusterNodesList:
    import capo_redshift.types.cluster_node

    out: ClusterNodesList = []
    for child in parent.findall(tag):
        out.append(capo_redshift.types.cluster_node.deserialize_query(child))
    return out
