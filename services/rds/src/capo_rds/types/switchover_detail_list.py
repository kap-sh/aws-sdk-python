"""Generated from Smithy shape ``com.amazonaws.rds#SwitchoverDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.switchover_detail

SwitchoverDetailList: TypeAlias = list[
    "capo_rds.types.switchover_detail.SwitchoverDetail"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: SwitchoverDetailList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.switchover_detail

    for n, item in enumerate(value, 1):
        capo_rds.types.switchover_detail.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> SwitchoverDetailList:
    import capo_rds.types.switchover_detail

    out: SwitchoverDetailList = []
    for child in el.findall("member"):
        out.append(capo_rds.types.switchover_detail.deserialize_query(child))
    return out


def serialize_query_flat(
    value: SwitchoverDetailList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.switchover_detail

    for n, item in enumerate(value, 1):
        capo_rds.types.switchover_detail.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> SwitchoverDetailList:
    import capo_rds.types.switchover_detail

    out: SwitchoverDetailList = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.switchover_detail.deserialize_query(child))
    return out
