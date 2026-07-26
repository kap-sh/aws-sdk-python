"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetails(TypedDict, closed=True):
    type: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The type of Elastic Graphics accelerator. </p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetails,
) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_json(
    data: dict,
) -> AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetails:
    out: AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetails = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    return out
