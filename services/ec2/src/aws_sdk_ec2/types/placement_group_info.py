"""Generated from Smithy shape ``com.amazonaws.ec2#PlacementGroupInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.placement_group_strategy_list


class PlacementGroupInfo(TypedDict):
    supported_strategies: NotRequired[
        "aws_sdk_ec2.types.placement_group_strategy_list.PlacementGroupStrategyList"
    ]
    """<p>The supported placement group types.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PlacementGroupInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "supported_strategies" in value:
        import aws_sdk_ec2.types.placement_group_strategy_list

        aws_sdk_ec2.types.placement_group_strategy_list.serialize_ec2_query(
            value["supported_strategies"], pairs, f"{prefix}.SupportedStrategies"
        )


def deserialize_ec2_query(el: Element) -> PlacementGroupInfo:
    out: PlacementGroupInfo = {}  # type: ignore[typeddict-item]
    if el.find("SupportedStrategies") is not None:
        import aws_sdk_ec2.types.placement_group_strategy_list

        out["supported_strategies"] = (
            aws_sdk_ec2.types.placement_group_strategy_list.deserialize_ec2_query(
                el, "SupportedStrategies"
            )
        )
    return out
