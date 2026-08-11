"""Generated from Smithy shape ``com.amazonaws.rds#DBParameterGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_parameter_group

DBParameterGroupList: TypeAlias = list[
    "capo_rds.types.db_parameter_group.DBParameterGroup"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBParameterGroupList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.db_parameter_group

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.db_parameter_group.serialize_query(
            item, pairs, f"{prefix}.DBParameterGroup.{n}"
        )


def deserialize_query(el: Element) -> DBParameterGroupList:
    import capo_rds.types.db_parameter_group

    out: DBParameterGroupList = []
    for child in el.findall("DBParameterGroup"):
        out.append(capo_rds.types.db_parameter_group.deserialize_query(child))
    return out


def serialize_query_flat(
    value: DBParameterGroupList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.db_parameter_group

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.db_parameter_group.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> DBParameterGroupList:
    import capo_rds.types.db_parameter_group

    out: DBParameterGroupList = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.db_parameter_group.deserialize_query(child))
    return out
