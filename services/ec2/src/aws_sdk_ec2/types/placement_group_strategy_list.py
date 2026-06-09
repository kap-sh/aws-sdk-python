"""Generated from Smithy shape ``com.amazonaws.ec2#PlacementGroupStrategyList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.placement_group_strategy

PlacementGroupStrategyList: TypeAlias = list[
    "aws_sdk_ec2.types.placement_group_strategy.PlacementGroupStrategy"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PlacementGroupStrategyList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.placement_group_strategy

        aws_sdk_ec2.types.placement_group_strategy.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> PlacementGroupStrategyList:
    import aws_sdk_ec2.types.placement_group_strategy

    out: PlacementGroupStrategyList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.placement_group_strategy.deserialize_ec2_query(child)
        )
    return out
