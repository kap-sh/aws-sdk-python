"""Generated from Smithy shape ``com.amazonaws.rds#DBClusterParameterGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_cluster_parameter_group

DBClusterParameterGroupList: TypeAlias = list[
    "capo_rds.types.db_cluster_parameter_group.DBClusterParameterGroup"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBClusterParameterGroupList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.db_cluster_parameter_group

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.db_cluster_parameter_group.serialize_query(
            item, pairs, f"{prefix}.DBClusterParameterGroup.{n}"
        )


def deserialize_query(el: Element) -> DBClusterParameterGroupList:
    import capo_rds.types.db_cluster_parameter_group

    out: DBClusterParameterGroupList = []
    for child in el.findall("DBClusterParameterGroup"):
        out.append(capo_rds.types.db_cluster_parameter_group.deserialize_query(child))
    return out


def serialize_query_flat(
    value: DBClusterParameterGroupList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.db_cluster_parameter_group

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.db_cluster_parameter_group.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> DBClusterParameterGroupList:
    import capo_rds.types.db_cluster_parameter_group

    out: DBClusterParameterGroupList = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.db_cluster_parameter_group.deserialize_query(child))
    return out
