"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceEventWindowTimeRangeList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_event_window_time_range

InstanceEventWindowTimeRangeList: TypeAlias = list[
    "aws_sdk_ec2.types.instance_event_window_time_range.InstanceEventWindowTimeRange"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceEventWindowTimeRangeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.instance_event_window_time_range

        aws_sdk_ec2.types.instance_event_window_time_range.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> InstanceEventWindowTimeRangeList:
    import aws_sdk_ec2.types.instance_event_window_time_range

    out: InstanceEventWindowTimeRangeList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.instance_event_window_time_range.deserialize_ec2_query(
                child
            )
        )
    return out
