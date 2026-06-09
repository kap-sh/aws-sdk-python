"""Generated from Smithy shape ``com.amazonaws.ec2#ScheduledInstanceSet``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.scheduled_instance

ScheduledInstanceSet: TypeAlias = list[
    "aws_sdk_ec2.types.scheduled_instance.ScheduledInstance"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ScheduledInstanceSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.scheduled_instance

        aws_sdk_ec2.types.scheduled_instance.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> ScheduledInstanceSet:
    import aws_sdk_ec2.types.scheduled_instance

    out: ScheduledInstanceSet = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.scheduled_instance.deserialize_ec2_query(child))
    return out
