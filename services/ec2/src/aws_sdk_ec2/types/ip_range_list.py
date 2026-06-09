"""Generated from Smithy shape ``com.amazonaws.ec2#IpRangeList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ip_range

IpRangeList: TypeAlias = list["aws_sdk_ec2.types.ip_range.IpRange"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpRangeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.ip_range

        aws_sdk_ec2.types.ip_range.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(parent: Element, tag: str) -> IpRangeList:
    import aws_sdk_ec2.types.ip_range

    out: IpRangeList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.ip_range.deserialize_ec2_query(child))
    return out
