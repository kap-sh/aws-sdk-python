"""Generated from Smithy shape ``com.amazonaws.neptune#DBClusterList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.db_cluster

DBClusterList: TypeAlias = list["capo_neptune.types.db_cluster.DBCluster"]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBClusterList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_neptune.types.db_cluster

    for n, item in enumerate(value, 1):
        capo_neptune.types.db_cluster.serialize_query(
            item, pairs, f"{prefix}.DBCluster.{n}"
        )


def deserialize_query(el: Element) -> DBClusterList:
    import capo_neptune.types.db_cluster

    out: DBClusterList = []
    for child in el.findall("DBCluster"):
        out.append(capo_neptune.types.db_cluster.deserialize_query(child))
    return out


def serialize_query_flat(
    value: DBClusterList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_neptune.types.db_cluster

    for n, item in enumerate(value, 1):
        capo_neptune.types.db_cluster.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> DBClusterList:
    import capo_neptune.types.db_cluster

    out: DBClusterList = []
    for child in parent.findall(tag):
        out.append(capo_neptune.types.db_cluster.deserialize_query(child))
    return out
