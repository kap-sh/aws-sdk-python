"""Generated from Smithy shape ``com.amazonaws.ec2#PlacementGroupInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.placement_group_strategy_list


class PlacementGroupInfo(TypedDict, closed=True):
    supported_strategies: NotRequired[
        "capo_ec2.types.placement_group_strategy_list.PlacementGroupStrategyList"
    ]
    """<p>The supported placement group types.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PlacementGroupInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "supported_strategies" in value:
        import capo_ec2.types.placement_group_strategy_list

        capo_ec2.types.placement_group_strategy_list.serialize_ec2_query(
            value["supported_strategies"], pairs, f"{key_prefix}SupportedStrategies"
        )


def deserialize_ec2_query(el: Element) -> PlacementGroupInfo:
    out: PlacementGroupInfo = {}  # type: ignore[typeddict-item]
    child_supported_strategies = el.find("supportedStrategies")
    if child_supported_strategies is not None:
        import capo_ec2.types.placement_group_strategy_list

        out["supported_strategies"] = (
            capo_ec2.types.placement_group_strategy_list.deserialize_ec2_query(
                child_supported_strategies
            )
        )
    return out
