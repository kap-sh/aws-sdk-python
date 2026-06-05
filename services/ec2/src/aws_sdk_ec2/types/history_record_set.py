"""Generated from Smithy shape ``com.amazonaws.ec2#HistoryRecordSet``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.history_record_entry

HistoryRecordSet: TypeAlias = list[
    "aws_sdk_ec2.types.history_record_entry.HistoryRecordEntry"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: HistoryRecordSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.history_record_entry

        aws_sdk_ec2.types.history_record_entry.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> HistoryRecordSet:
    import aws_sdk_ec2.types.history_record_entry

    out: HistoryRecordSet = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.history_record_entry.deserialize_ec2_query(child))
    return out
