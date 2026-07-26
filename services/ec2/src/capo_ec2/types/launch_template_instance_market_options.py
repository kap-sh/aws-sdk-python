"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateInstanceMarketOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.launch_template_spot_market_options
    import capo_ec2.types.market_type


class LaunchTemplateInstanceMarketOptions(TypedDict, closed=True):
    market_type: NotRequired["capo_ec2.types.market_type.MarketType"]
    """<p>The market type.</p>"""
    spot_options: NotRequired[
        "capo_ec2.types.launch_template_spot_market_options.LaunchTemplateSpotMarketOptions"
    ]
    """<p>The options for Spot Instances.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LaunchTemplateInstanceMarketOptions,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "market_type" in value:
        import capo_ec2.types.market_type

        capo_ec2.types.market_type.serialize_ec2_query(
            value["market_type"], pairs, f"{prefix}.MarketType"
        )
    if "spot_options" in value:
        import capo_ec2.types.launch_template_spot_market_options

        capo_ec2.types.launch_template_spot_market_options.serialize_ec2_query(
            value["spot_options"], pairs, f"{prefix}.SpotOptions"
        )


def deserialize_ec2_query(el: Element) -> LaunchTemplateInstanceMarketOptions:
    out: LaunchTemplateInstanceMarketOptions = {}  # type: ignore[typeddict-item]
    child_market_type = el.find("MarketType")
    if child_market_type is not None:
        import capo_ec2.types.market_type

        out["market_type"] = capo_ec2.types.market_type.deserialize_ec2_query(
            child_market_type
        )
    child_spot_options = el.find("SpotOptions")
    if child_spot_options is not None:
        import capo_ec2.types.launch_template_spot_market_options

        out["spot_options"] = (
            capo_ec2.types.launch_template_spot_market_options.deserialize_ec2_query(
                child_spot_options
            )
        )
    return out
