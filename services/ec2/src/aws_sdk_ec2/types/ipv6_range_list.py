"""Generated from Smithy shape ``com.amazonaws.ec2#Ipv6RangeList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipv6_range

Ipv6RangeList: TypeAlias = list["aws_sdk_ec2.types.ipv6_range.Ipv6Range"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: Ipv6RangeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.ipv6_range

        aws_sdk_ec2.types.ipv6_range.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(parent: Element, tag: str) -> Ipv6RangeList:
    import aws_sdk_ec2.types.ipv6_range

    out: Ipv6RangeList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.ipv6_range.deserialize_ec2_query(child))
    return out
