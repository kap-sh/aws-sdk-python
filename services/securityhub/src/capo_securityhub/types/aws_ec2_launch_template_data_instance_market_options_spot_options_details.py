"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.integer
    import capo_securityhub.types.non_empty_string


class AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetails(
    TypedDict, closed=True
):
    block_duration_minutes: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p> Deprecated. </p>"""
    instance_interruption_behavior: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The behavior when a Spot Instance is interrupted. </p>"""
    max_price: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The maximum hourly price you're willing to pay for the Spot Instances. </p>"""
    spot_instance_type: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The Spot Instance request type. </p>"""
    valid_until: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The end date of the request, in UTC format (YYYY-MM-DDTHH:MM:SSZ), for persistent requests. </p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetails,
) -> dict:
    out: dict = {}
    if "block_duration_minutes" in value:
        out["BlockDurationMinutes"] = value["block_duration_minutes"]
    if "instance_interruption_behavior" in value:
        out["InstanceInterruptionBehavior"] = value["instance_interruption_behavior"]
    if "max_price" in value:
        out["MaxPrice"] = value["max_price"]
    if "spot_instance_type" in value:
        out["SpotInstanceType"] = value["spot_instance_type"]
    if "valid_until" in value:
        out["ValidUntil"] = value["valid_until"]
    return out


def deserialize_json(
    data: dict,
) -> AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetails:
    out: AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetails = {}  # type: ignore[typeddict-item]
    if "BlockDurationMinutes" in data:
        out["block_duration_minutes"] = data["BlockDurationMinutes"]
    if "InstanceInterruptionBehavior" in data:
        out["instance_interruption_behavior"] = data["InstanceInterruptionBehavior"]
    if "MaxPrice" in data:
        out["max_price"] = data["MaxPrice"]
    if "SpotInstanceType" in data:
        out["spot_instance_type"] = data["SpotInstanceType"]
    if "ValidUntil" in data:
        out["valid_until"] = data["ValidUntil"]
    return out
