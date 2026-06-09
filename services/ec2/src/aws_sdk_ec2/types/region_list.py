"""Generated from Smithy shape ``com.amazonaws.ec2#RegionList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.region

RegionList: TypeAlias = list["aws_sdk_ec2.types.region.Region"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RegionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.region

        aws_sdk_ec2.types.region.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(parent: Element, tag: str) -> RegionList:
    import aws_sdk_ec2.types.region

    out: RegionList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.region.deserialize_ec2_query(child))
    return out
