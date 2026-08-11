"""Generated from Smithy shape ``com.amazonaws.rds#DBClusterStatusInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_cluster_status_info

DBClusterStatusInfoList: TypeAlias = list[
    "capo_rds.types.db_cluster_status_info.DBClusterStatusInfo"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBClusterStatusInfoList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.db_cluster_status_info

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.db_cluster_status_info.serialize_query(
            item, pairs, f"{prefix}.DBClusterStatusInfo.{n}"
        )


def deserialize_query(el: Element) -> DBClusterStatusInfoList:
    import capo_rds.types.db_cluster_status_info

    out: DBClusterStatusInfoList = []
    for child in el.findall("DBClusterStatusInfo"):
        out.append(capo_rds.types.db_cluster_status_info.deserialize_query(child))
    return out


def serialize_query_flat(
    value: DBClusterStatusInfoList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.db_cluster_status_info

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.db_cluster_status_info.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> DBClusterStatusInfoList:
    import capo_rds.types.db_cluster_status_info

    out: DBClusterStatusInfoList = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.db_cluster_status_info.deserialize_query(child))
    return out
