"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceStatusEventList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_status_event

InstanceStatusEventList: TypeAlias = list[
    "aws_sdk_ec2.types.instance_status_event.InstanceStatusEvent"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceStatusEventList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.instance_status_event

        aws_sdk_ec2.types.instance_status_event.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> InstanceStatusEventList:
    import aws_sdk_ec2.types.instance_status_event

    out: InstanceStatusEventList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.instance_status_event.deserialize_ec2_query(child))
    return out
