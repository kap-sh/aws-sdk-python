"""Generated from Smithy shape ``com.amazonaws.ec2#GroupBySet``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.group_by

GroupBySet: TypeAlias = list["aws_sdk_ec2.types.group_by.GroupBy"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GroupBySet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.group_by

        aws_sdk_ec2.types.group_by.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(parent: Element, tag: str) -> GroupBySet:
    import aws_sdk_ec2.types.group_by

    out: GroupBySet = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.group_by.deserialize_ec2_query(child))
    return out
