"""Generated from Smithy shape ``com.amazonaws.rds#DBProxyList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_proxy

DBProxyList: TypeAlias = list["capo_rds.types.db_proxy.DBProxy"]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBProxyList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.db_proxy

    for n, item in enumerate(value, 1):
        capo_rds.types.db_proxy.serialize_query(item, pairs, f"{prefix}.member.{n}")


def deserialize_query(el: Element) -> DBProxyList:
    import capo_rds.types.db_proxy

    out: DBProxyList = []
    for child in el.findall("member"):
        out.append(capo_rds.types.db_proxy.deserialize_query(child))
    return out


def serialize_query_flat(
    value: DBProxyList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.db_proxy

    for n, item in enumerate(value, 1):
        capo_rds.types.db_proxy.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> DBProxyList:
    import capo_rds.types.db_proxy

    out: DBProxyList = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.db_proxy.deserialize_query(child))
    return out
