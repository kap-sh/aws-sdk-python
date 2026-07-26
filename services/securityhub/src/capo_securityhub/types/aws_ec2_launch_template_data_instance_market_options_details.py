"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2LaunchTemplateDataInstanceMarketOptionsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ec2_launch_template_data_instance_market_options_spot_options_details
    import capo_securityhub.types.non_empty_string


class AwsEc2LaunchTemplateDataInstanceMarketOptionsDetails(TypedDict, closed=True):
    market_type: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The market type. </p>"""
    spot_options: NotRequired[
        "capo_securityhub.types.aws_ec2_launch_template_data_instance_market_options_spot_options_details.AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetails"
    ]
    """<p> The options for Spot Instances. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2LaunchTemplateDataInstanceMarketOptionsDetails) -> dict:
    out: dict = {}
    if "market_type" in value:
        out["MarketType"] = value["market_type"]
    if "spot_options" in value:
        import capo_securityhub.types.aws_ec2_launch_template_data_instance_market_options_spot_options_details

        out["SpotOptions"] = (
            capo_securityhub.types.aws_ec2_launch_template_data_instance_market_options_spot_options_details.serialize_json(
                value["spot_options"]
            )
        )
    return out


def deserialize_json(
    data: dict,
) -> AwsEc2LaunchTemplateDataInstanceMarketOptionsDetails:
    out: AwsEc2LaunchTemplateDataInstanceMarketOptionsDetails = {}  # type: ignore[typeddict-item]
    if "MarketType" in data:
        out["market_type"] = data["MarketType"]
    if "SpotOptions" in data:
        import capo_securityhub.types.aws_ec2_launch_template_data_instance_market_options_spot_options_details

        out["spot_options"] = (
            capo_securityhub.types.aws_ec2_launch_template_data_instance_market_options_spot_options_details.deserialize_json(
                data["SpotOptions"]
            )
        )
    return out
