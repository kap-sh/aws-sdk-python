"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceEventWindowTimeRangeRequestSet``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_event_window_time_range_request

InstanceEventWindowTimeRangeRequestSet: TypeAlias = list[
    "aws_sdk_ec2.types.instance_event_window_time_range_request.InstanceEventWindowTimeRangeRequest"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceEventWindowTimeRangeRequestSet,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.instance_event_window_time_range_request

        aws_sdk_ec2.types.instance_event_window_time_range_request.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> InstanceEventWindowTimeRangeRequestSet:
    import aws_sdk_ec2.types.instance_event_window_time_range_request

    out: InstanceEventWindowTimeRangeRequestSet = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.instance_event_window_time_range_request.deserialize_ec2_query(
                child
            )
        )
    return out
