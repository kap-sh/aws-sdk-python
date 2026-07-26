"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.integer


class AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetails(
    TypedDict, closed=True
):
    max: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p> The maximum number of accelerators. If this parameter isn't specified, there's no maximum limit. To exclude accelerator-enabled instance types, set <code>Max</code> to <code>0</code>. </p>"""
    min: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p> The minimum number of accelerators. If this parameter isn't specified, there's no minimum limit. </p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetails,
) -> dict:
    out: dict = {}
    if "max" in value:
        out["Max"] = value["max"]
    if "min" in value:
        out["Min"] = value["min"]
    return out


def deserialize_json(
    data: dict,
) -> AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetails:
    out: AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetails = {}  # type: ignore[typeddict-item]
    if "Max" in data:
        out["max"] = data["Max"]
    if "Min" in data:
        out["min"] = data["Min"]
    return out
