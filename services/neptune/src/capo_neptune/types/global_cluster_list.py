"""Generated from Smithy shape ``com.amazonaws.neptune#GlobalClusterList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.global_cluster

GlobalClusterList: TypeAlias = list["capo_neptune.types.global_cluster.GlobalCluster"]


# --- awsQuery ser/de ---
def serialize_query(
    value: GlobalClusterList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_neptune.types.global_cluster

    for n, item in enumerate(value, 1):
        capo_neptune.types.global_cluster.serialize_query(
            item, pairs, f"{prefix}.GlobalClusterMember.{n}"
        )


def deserialize_query(el: Element) -> GlobalClusterList:
    import capo_neptune.types.global_cluster

    out: GlobalClusterList = []
    for child in el.findall("GlobalClusterMember"):
        out.append(capo_neptune.types.global_cluster.deserialize_query(child))
    return out


def serialize_query_flat(
    value: GlobalClusterList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_neptune.types.global_cluster

    for n, item in enumerate(value, 1):
        capo_neptune.types.global_cluster.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> GlobalClusterList:
    import capo_neptune.types.global_cluster

    out: GlobalClusterList = []
    for child in parent.findall(tag):
        out.append(capo_neptune.types.global_cluster.deserialize_query(child))
    return out
