"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeletePartnerAppRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.client_token
    import capo_sagemaker.types.partner_app_arn


class DeletePartnerAppRequest(TypedDict, closed=True):
    arn: NotRequired["capo_sagemaker.types.partner_app_arn.PartnerAppArn"]
    """<p>The ARN of the SageMaker Partner AI App to delete.</p>"""
    client_token: NotRequired["capo_sagemaker.types.client_token.ClientToken"]
    """<p>A unique token that guarantees that the call to this API is idempotent.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeletePartnerAppRequest) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeletePartnerAppRequest:
    out: DeletePartnerAppRequest = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
