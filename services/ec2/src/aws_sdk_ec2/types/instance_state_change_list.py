"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceStateChangeList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_state_change

InstanceStateChangeList: TypeAlias = list[
    "aws_sdk_ec2.types.instance_state_change.InstanceStateChange"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceStateChangeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.instance_state_change

        aws_sdk_ec2.types.instance_state_change.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> InstanceStateChangeList:
    import aws_sdk_ec2.types.instance_state_change

    out: InstanceStateChangeList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.instance_state_change.deserialize_ec2_query(child))
    return out
