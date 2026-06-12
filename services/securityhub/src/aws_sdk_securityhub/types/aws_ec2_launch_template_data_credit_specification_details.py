"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2LaunchTemplateDataCreditSpecificationDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsEc2LaunchTemplateDataCreditSpecificationDetails(TypedDict):
    cpu_credits: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The credit option for CPU usage of a T instance. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2LaunchTemplateDataCreditSpecificationDetails) -> dict:
    out: dict = {}
    if "cpu_credits" in value:
        out["CpuCredits"] = value["cpu_credits"]
    return out


def deserialize_json(data: dict) -> AwsEc2LaunchTemplateDataCreditSpecificationDetails:
    out: AwsEc2LaunchTemplateDataCreditSpecificationDetails = {}  # type: ignore[typeddict-item]
    if "CpuCredits" in data:
        out["cpu_credits"] = data["CpuCredits"]
    return out
