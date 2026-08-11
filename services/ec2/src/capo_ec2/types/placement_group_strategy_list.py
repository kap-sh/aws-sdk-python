"""Generated from Smithy shape ``com.amazonaws.ec2#PlacementGroupStrategyList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.placement_group_strategy

PlacementGroupStrategyList: TypeAlias = list[
    "capo_ec2.types.placement_group_strategy.PlacementGroupStrategy"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PlacementGroupStrategyList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.placement_group_strategy

        capo_ec2.types.placement_group_strategy.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> PlacementGroupStrategyList:
    import capo_ec2.types.placement_group_strategy

    out: PlacementGroupStrategyList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.placement_group_strategy.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> PlacementGroupStrategyList:
    import capo_ec2.types.placement_group_strategy

    out: PlacementGroupStrategyList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.placement_group_strategy.deserialize_ec2_query(child))
    return out
