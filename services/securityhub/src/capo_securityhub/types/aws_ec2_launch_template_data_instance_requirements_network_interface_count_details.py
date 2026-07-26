"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.integer


class AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetails(
    TypedDict, closed=True
):
    max: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p> The maximum number of network interfaces. </p>"""
    min: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p> The minimum number of network interfaces. </p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetails,
) -> dict:
    out: dict = {}
    if "max" in value:
        out["Max"] = value["max"]
    if "min" in value:
        out["Min"] = value["min"]
    return out


def deserialize_json(
    data: dict,
) -> AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetails:
    out: AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetails = {}  # type: ignore[typeddict-item]
    if "Max" in data:
        out["max"] = data["Max"]
    if "Min" in data:
        out["min"] = data["Min"]
    return out
