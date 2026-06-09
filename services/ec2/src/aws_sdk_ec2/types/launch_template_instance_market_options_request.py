"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateInstanceMarketOptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.launch_template_spot_market_options_request
    import aws_sdk_ec2.types.market_type


class LaunchTemplateInstanceMarketOptionsRequest(TypedDict):
    market_type: NotRequired["aws_sdk_ec2.types.market_type.MarketType"]
    """<p>The market type.</p>"""
    spot_options: NotRequired[
        "aws_sdk_ec2.types.launch_template_spot_market_options_request.LaunchTemplateSpotMarketOptionsRequest"
    ]
    """<p>The options for Spot Instances.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LaunchTemplateInstanceMarketOptionsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "market_type" in value:
        import aws_sdk_ec2.types.market_type

        aws_sdk_ec2.types.market_type.serialize_ec2_query(
            value["market_type"], pairs, f"{prefix}.MarketType"
        )
    if "spot_options" in value:
        import aws_sdk_ec2.types.launch_template_spot_market_options_request

        aws_sdk_ec2.types.launch_template_spot_market_options_request.serialize_ec2_query(
            value["spot_options"], pairs, f"{prefix}.SpotOptions"
        )


def deserialize_ec2_query(el: Element) -> LaunchTemplateInstanceMarketOptionsRequest:
    out: LaunchTemplateInstanceMarketOptionsRequest = {}  # type: ignore[typeddict-item]
    child_market_type = el.find("MarketType")
    if child_market_type is not None:
        import aws_sdk_ec2.types.market_type

        out["market_type"] = aws_sdk_ec2.types.market_type.deserialize_ec2_query(
            child_market_type
        )
    child_spot_options = el.find("SpotOptions")
    if child_spot_options is not None:
        import aws_sdk_ec2.types.launch_template_spot_market_options_request

        out["spot_options"] = (
            aws_sdk_ec2.types.launch_template_spot_market_options_request.deserialize_ec2_query(
                child_spot_options
            )
        )
    return out
