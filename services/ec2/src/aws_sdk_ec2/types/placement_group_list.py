"""Generated from Smithy shape ``com.amazonaws.ec2#PlacementGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.placement_group

PlacementGroupList: TypeAlias = list["aws_sdk_ec2.types.placement_group.PlacementGroup"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PlacementGroupList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.placement_group

        aws_sdk_ec2.types.placement_group.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> PlacementGroupList:
    import aws_sdk_ec2.types.placement_group

    out: PlacementGroupList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.placement_group.deserialize_ec2_query(child))
    return out
