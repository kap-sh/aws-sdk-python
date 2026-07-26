"""Generated from Smithy shape ``com.amazonaws.redshift#DataShareList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.data_share

DataShareList: TypeAlias = list["capo_redshift.types.data_share.DataShare"]


# --- awsQuery ser/de ---
def serialize_query(
    value: DataShareList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.data_share

    for n, item in enumerate(value, 1):
        capo_redshift.types.data_share.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> DataShareList:
    import capo_redshift.types.data_share

    out: DataShareList = []
    for child in el.findall("member"):
        out.append(capo_redshift.types.data_share.deserialize_query(child))
    return out


def serialize_query_flat(
    value: DataShareList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.data_share

    for n, item in enumerate(value, 1):
        capo_redshift.types.data_share.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> DataShareList:
    import capo_redshift.types.data_share

    out: DataShareList = []
    for child in parent.findall(tag):
        out.append(capo_redshift.types.data_share.deserialize_query(child))
    return out
