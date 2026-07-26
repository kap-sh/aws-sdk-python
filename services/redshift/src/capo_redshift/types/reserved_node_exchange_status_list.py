"""Generated from Smithy shape ``com.amazonaws.redshift#ReservedNodeExchangeStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.reserved_node_exchange_status

ReservedNodeExchangeStatusList: TypeAlias = list[
    "capo_redshift.types.reserved_node_exchange_status.ReservedNodeExchangeStatus"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ReservedNodeExchangeStatusList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.reserved_node_exchange_status

    for n, item in enumerate(value, 1):
        capo_redshift.types.reserved_node_exchange_status.serialize_query(
            item, pairs, f"{prefix}.ReservedNodeExchangeStatus.{n}"
        )


def deserialize_query(el: Element) -> ReservedNodeExchangeStatusList:
    import capo_redshift.types.reserved_node_exchange_status

    out: ReservedNodeExchangeStatusList = []
    for child in el.findall("ReservedNodeExchangeStatus"):
        out.append(
            capo_redshift.types.reserved_node_exchange_status.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: ReservedNodeExchangeStatusList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.reserved_node_exchange_status

    for n, item in enumerate(value, 1):
        capo_redshift.types.reserved_node_exchange_status.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ReservedNodeExchangeStatusList:
    import capo_redshift.types.reserved_node_exchange_status

    out: ReservedNodeExchangeStatusList = []
    for child in parent.findall(tag):
        out.append(
            capo_redshift.types.reserved_node_exchange_status.deserialize_query(child)
        )
    return out
