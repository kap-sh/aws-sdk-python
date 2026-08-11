"""Generated from Smithy shape ``com.amazonaws.rds#DBClusterEndpointList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_cluster_endpoint

DBClusterEndpointList: TypeAlias = list[
    "capo_rds.types.db_cluster_endpoint.DBClusterEndpoint"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBClusterEndpointList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.db_cluster_endpoint

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.db_cluster_endpoint.serialize_query(
            item, pairs, f"{prefix}.DBClusterEndpointList.{n}"
        )


def deserialize_query(el: Element) -> DBClusterEndpointList:
    import capo_rds.types.db_cluster_endpoint

    out: DBClusterEndpointList = []
    for child in el.findall("DBClusterEndpointList"):
        out.append(capo_rds.types.db_cluster_endpoint.deserialize_query(child))
    return out


def serialize_query_flat(
    value: DBClusterEndpointList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.db_cluster_endpoint

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.db_cluster_endpoint.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> DBClusterEndpointList:
    import capo_rds.types.db_cluster_endpoint

    out: DBClusterEndpointList = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.db_cluster_endpoint.deserialize_query(child))
    return out
