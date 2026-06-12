"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string


class AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetails(TypedDict):
    count: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p> The number of Elastic Inference accelerators to attach to the instance. </p>"""
    type: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The type of Elastic Inference accelerator. </p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetails,
) -> dict:
    out: dict = {}
    if "count" in value:
        out["Count"] = value["count"]
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_json(
    data: dict,
) -> AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetails:
    out: AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetails = {}  # type: ignore[typeddict-item]
    if "Count" in data:
        out["count"] = data["Count"]
    if "Type" in data:
        out["type"] = data["Type"]
    return out
