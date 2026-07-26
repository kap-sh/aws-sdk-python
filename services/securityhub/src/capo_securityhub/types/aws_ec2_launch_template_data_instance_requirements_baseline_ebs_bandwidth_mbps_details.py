"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.integer


class AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetails(
    TypedDict, closed=True
):
    max: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p> The maximum baseline bandwidth, in Mbps. If this parameter is omitted, there's no maximum limit. </p>"""
    min: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p> The minimum baseline bandwidth, in Mbps. If this parameter is omitted, there's no minimum limit. </p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetails,
) -> dict:
    out: dict = {}
    if "max" in value:
        out["Max"] = value["max"]
    if "min" in value:
        out["Min"] = value["min"]
    return out


def deserialize_json(
    data: dict,
) -> AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetails:
    out: AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetails = {}  # type: ignore[typeddict-item]
    if "Max" in data:
        out["max"] = data["Max"]
    if "Min" in data:
        out["min"] = data["Min"]
    return out
