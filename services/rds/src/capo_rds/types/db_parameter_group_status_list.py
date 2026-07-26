"""Generated from Smithy shape ``com.amazonaws.rds#DBParameterGroupStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_parameter_group_status

DBParameterGroupStatusList: TypeAlias = list[
    "capo_rds.types.db_parameter_group_status.DBParameterGroupStatus"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBParameterGroupStatusList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.db_parameter_group_status

    for n, item in enumerate(value, 1):
        capo_rds.types.db_parameter_group_status.serialize_query(
            item, pairs, f"{prefix}.DBParameterGroup.{n}"
        )


def deserialize_query(el: Element) -> DBParameterGroupStatusList:
    import capo_rds.types.db_parameter_group_status

    out: DBParameterGroupStatusList = []
    for child in el.findall("DBParameterGroup"):
        out.append(capo_rds.types.db_parameter_group_status.deserialize_query(child))
    return out


def serialize_query_flat(
    value: DBParameterGroupStatusList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.db_parameter_group_status

    for n, item in enumerate(value, 1):
        capo_rds.types.db_parameter_group_status.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> DBParameterGroupStatusList:
    import capo_rds.types.db_parameter_group_status

    out: DBParameterGroupStatusList = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.db_parameter_group_status.deserialize_query(child))
    return out
