"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateHubContentReferenceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.hub_arn
    import capo_sagemaker.types.hub_content_arn


class UpdateHubContentReferenceResponse(TypedDict, closed=True):
    hub_arn: NotRequired["capo_sagemaker.types.hub_arn.HubArn"]
    """<p>The ARN of the private model hub that contains the updated hub content.</p>"""
    hub_content_arn: NotRequired["capo_sagemaker.types.hub_content_arn.HubContentArn"]
    """<p>The ARN of the hub content resource that was updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateHubContentReferenceResponse) -> dict:
    out: dict = {}
    if "hub_arn" in value:
        out["HubArn"] = value["hub_arn"]
    if "hub_content_arn" in value:
        out["HubContentArn"] = value["hub_content_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateHubContentReferenceResponse:
    out: UpdateHubContentReferenceResponse = {}  # type: ignore[typeddict-item]
    if "HubArn" in data:
        out["hub_arn"] = data["HubArn"]
    if "HubContentArn" in data:
        out["hub_content_arn"] = data["HubContentArn"]
    return out
