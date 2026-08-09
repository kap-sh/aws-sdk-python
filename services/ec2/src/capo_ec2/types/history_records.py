"""Generated from Smithy shape ``com.amazonaws.ec2#HistoryRecords``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.history_record

HistoryRecords: TypeAlias = list["capo_ec2.types.history_record.HistoryRecord"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: HistoryRecords, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.history_record

        capo_ec2.types.history_record.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(el: Element) -> HistoryRecords:
    import capo_ec2.types.history_record

    out: HistoryRecords = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.history_record.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> HistoryRecords:
    import capo_ec2.types.history_record

    out: HistoryRecords = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.history_record.deserialize_ec2_query(child))
    return out
