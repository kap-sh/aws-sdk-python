"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreatePartnerAppResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.partner_app_arn


class CreatePartnerAppResponse(TypedDict, closed=True):
    arn: NotRequired["capo_sagemaker.types.partner_app_arn.PartnerAppArn"]
    """<p>The ARN of the SageMaker Partner AI App.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePartnerAppResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePartnerAppResponse:
    out: CreatePartnerAppResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
