"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetails(
    TypedDict, closed=True
):
    value: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the Availability Zone.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetails,
) -> dict:
    out: dict = {}
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(
    data: dict,
) -> AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetails:
    out: AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetails = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
