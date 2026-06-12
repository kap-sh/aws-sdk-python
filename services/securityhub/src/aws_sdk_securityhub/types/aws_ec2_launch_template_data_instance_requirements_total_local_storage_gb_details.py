"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.double


class AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetails(TypedDict):
    max: NotRequired["aws_sdk_securityhub.types.double.Double"]
    """<p> The maximum amount of total local storage, in GB. </p>"""
    min: NotRequired["aws_sdk_securityhub.types.double.Double"]
    """<p> The minimum amount of total local storage, in GB. </p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetails,
) -> dict:
    out: dict = {}
    if "max" in value:
        out["Max"] = value["max"]
    if "min" in value:
        out["Min"] = value["min"]
    return out


def deserialize_json(
    data: dict,
) -> AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetails:
    out: AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetails = {}  # type: ignore[typeddict-item]
    if "Max" in data:
        out["max"] = data["Max"]
    if "Min" in data:
        out["min"] = data["Min"]
    return out
