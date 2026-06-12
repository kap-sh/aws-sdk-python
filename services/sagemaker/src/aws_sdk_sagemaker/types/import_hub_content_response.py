"""Generated from Smithy shape ``com.amazonaws.sagemaker#ImportHubContentResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.hub_arn
    import aws_sdk_sagemaker.types.hub_content_arn


class ImportHubContentResponse(TypedDict):
    hub_arn: NotRequired["aws_sdk_sagemaker.types.hub_arn.HubArn"]
    """<p>The ARN of the hub that the content was imported into.</p>"""
    hub_content_arn: NotRequired[
        "aws_sdk_sagemaker.types.hub_content_arn.HubContentArn"
    ]
    """<p>The ARN of the hub content that was imported.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportHubContentResponse) -> dict:
    out: dict = {}
    if "hub_arn" in value:
        out["HubArn"] = value["hub_arn"]
    if "hub_content_arn" in value:
        out["HubContentArn"] = value["hub_content_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportHubContentResponse:
    out: ImportHubContentResponse = {}  # type: ignore[typeddict-item]
    if "HubArn" in data:
        out["hub_arn"] = data["HubArn"]
    if "HubContentArn" in data:
        out["hub_content_arn"] = data["HubContentArn"]
    return out
