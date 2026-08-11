"""Generated from Smithy shape ``com.amazonaws.rds#OrderableDBInstanceOptionsList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.orderable_db_instance_option

OrderableDBInstanceOptionsList: TypeAlias = list[
    "capo_rds.types.orderable_db_instance_option.OrderableDBInstanceOption"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: OrderableDBInstanceOptionsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.orderable_db_instance_option

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.orderable_db_instance_option.serialize_query(
            item, pairs, f"{prefix}.OrderableDBInstanceOption.{n}"
        )


def deserialize_query(el: Element) -> OrderableDBInstanceOptionsList:
    import capo_rds.types.orderable_db_instance_option

    out: OrderableDBInstanceOptionsList = []
    for child in el.findall("OrderableDBInstanceOption"):
        out.append(capo_rds.types.orderable_db_instance_option.deserialize_query(child))
    return out


def serialize_query_flat(
    value: OrderableDBInstanceOptionsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.orderable_db_instance_option

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.orderable_db_instance_option.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> OrderableDBInstanceOptionsList:
    import capo_rds.types.orderable_db_instance_option

    out: OrderableDBInstanceOptionsList = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.orderable_db_instance_option.deserialize_query(child))
    return out
