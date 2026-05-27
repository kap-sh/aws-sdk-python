"""Generated from Smithy shape ``com.amazonaws.s3#PartitionedPrefix``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.partition_date_source


class PartitionedPrefix(TypedDict):
    partition_date_source: NotRequired[
        "aws_sdk_s3.types.partition_date_source.PartitionDateSource"
    ]
    """<p>Specifies the partition date source for the partitioned prefix. <code>PartitionDateSource</code> can be <code>EventTime</code> or <code>DeliveryTime</code>.</p> <p>For <code>DeliveryTime</code>, the time in the log file names corresponds to the delivery time for the log files. </p> <p> For <code>EventTime</code>, The logs delivered are for a specific day only. The year, month, and day correspond to the day on which the event occurred, and the hour, minutes and seconds are set to 00 in the key.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: PartitionedPrefix, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "partition_date_source" in value:
        import aws_sdk_s3.types.partition_date_source

        aws_sdk_s3.types.partition_date_source.serialize_xml(
            value["partition_date_source"], el, "PartitionDateSource"
        )


def deserialize_xml(el: Element) -> PartitionedPrefix:
    out: PartitionedPrefix = {}  # type: ignore[typeddict-item]
    child_partition_date_source = el.find("PartitionDateSource")
    if child_partition_date_source is not None:
        import aws_sdk_s3.types.partition_date_source

        out["partition_date_source"] = (
            aws_sdk_s3.types.partition_date_source.deserialize_xml(
                child_partition_date_source
            )
        )
    return out
