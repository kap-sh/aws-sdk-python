"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.double


class AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetails(TypedDict):
    max: NotRequired["aws_sdk_securityhub.types.double.Double"]
    """<p> The maximum amount of memory per vCPU, in GiB. If this parameter is omitted, there's no maximum limit. </p>"""
    min: NotRequired["aws_sdk_securityhub.types.double.Double"]
    """<p> The minimum amount of memory per vCPU, in GiB. If this parameter is omitted, there's no maximum limit. </p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetails,
) -> dict:
    out: dict = {}
    if "max" in value:
        out["Max"] = value["max"]
    if "min" in value:
        out["Min"] = value["min"]
    return out


def deserialize_json(
    data: dict,
) -> AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetails:
    out: AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetails = {}  # type: ignore[typeddict-item]
    if "Max" in data:
        out["max"] = data["Max"]
    if "Min" in data:
        out["min"] = data["Min"]
    return out
