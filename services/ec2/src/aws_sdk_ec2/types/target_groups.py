"""Generated from Smithy shape ``com.amazonaws.ec2#TargetGroups``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.target_group

TargetGroups: TypeAlias = list["aws_sdk_ec2.types.target_group.TargetGroup"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TargetGroups, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.target_group

        aws_sdk_ec2.types.target_group.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(parent: Element, tag: str) -> TargetGroups:
    import aws_sdk_ec2.types.target_group

    out: TargetGroups = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.target_group.deserialize_ec2_query(child))
    return out
