"""Generated from Smithy shape ``com.amazonaws.redshift#SubnetList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.subnet

SubnetList: TypeAlias = list["capo_redshift.types.subnet.Subnet"]


# --- awsQuery ser/de ---
def serialize_query(
    value: SubnetList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.subnet

    for n, item in enumerate(value, 1):
        capo_redshift.types.subnet.serialize_query(item, pairs, f"{prefix}.Subnet.{n}")


def deserialize_query(el: Element) -> SubnetList:
    import capo_redshift.types.subnet

    out: SubnetList = []
    for child in el.findall("Subnet"):
        out.append(capo_redshift.types.subnet.deserialize_query(child))
    return out


def serialize_query_flat(
    value: SubnetList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.subnet

    for n, item in enumerate(value, 1):
        capo_redshift.types.subnet.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> SubnetList:
    import capo_redshift.types.subnet

    out: SubnetList = []
    for child in parent.findall(tag):
        out.append(capo_redshift.types.subnet.deserialize_query(child))
    return out
