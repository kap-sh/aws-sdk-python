"""Generated from Smithy shape ``com.amazonaws.ec2#HistoryRecords``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.history_record

HistoryRecords: TypeAlias = list["aws_sdk_ec2.types.history_record.HistoryRecord"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: HistoryRecords, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.history_record

        aws_sdk_ec2.types.history_record.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> HistoryRecords:
    import aws_sdk_ec2.types.history_record

    out: HistoryRecords = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.history_record.deserialize_ec2_query(child))
    return out
