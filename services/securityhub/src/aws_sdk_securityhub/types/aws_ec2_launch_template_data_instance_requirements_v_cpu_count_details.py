"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.integer


class AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetails(TypedDict):
    max: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p> The maximum number of vCPUs. </p>"""
    min: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p> The minimum number of vCPUs. </p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetails,
) -> dict:
    out: dict = {}
    if "max" in value:
        out["Max"] = value["max"]
    if "min" in value:
        out["Min"] = value["min"]
    return out


def deserialize_json(
    data: dict,
) -> AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetails:
    out: AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetails = {}  # type: ignore[typeddict-item]
    if "Max" in data:
        out["max"] = data["Max"]
    if "Min" in data:
        out["min"] = data["Min"]
    return out
