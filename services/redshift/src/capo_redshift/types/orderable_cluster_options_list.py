"""Generated from Smithy shape ``com.amazonaws.redshift#OrderableClusterOptionsList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.orderable_cluster_option

OrderableClusterOptionsList: TypeAlias = list[
    "capo_redshift.types.orderable_cluster_option.OrderableClusterOption"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: OrderableClusterOptionsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.orderable_cluster_option

    for n, item in enumerate(value, 1):
        capo_redshift.types.orderable_cluster_option.serialize_query(
            item, pairs, f"{prefix}.OrderableClusterOption.{n}"
        )


def deserialize_query(el: Element) -> OrderableClusterOptionsList:
    import capo_redshift.types.orderable_cluster_option

    out: OrderableClusterOptionsList = []
    for child in el.findall("OrderableClusterOption"):
        out.append(
            capo_redshift.types.orderable_cluster_option.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: OrderableClusterOptionsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.orderable_cluster_option

    for n, item in enumerate(value, 1):
        capo_redshift.types.orderable_cluster_option.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> OrderableClusterOptionsList:
    import capo_redshift.types.orderable_cluster_option

    out: OrderableClusterOptionsList = []
    for child in parent.findall(tag):
        out.append(
            capo_redshift.types.orderable_cluster_option.deserialize_query(child)
        )
    return out
