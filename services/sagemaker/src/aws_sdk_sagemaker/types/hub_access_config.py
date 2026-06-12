"""Generated from Smithy shape ``com.amazonaws.sagemaker#HubAccessConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.hub_content_arn


class HubAccessConfig(TypedDict):
    hub_content_arn: NotRequired[
        "aws_sdk_sagemaker.types.hub_content_arn.HubContentArn"
    ]
    """<p>The ARN of your private model hub content. This should be a <code>ModelReference</code> resource type that points to a SageMaker JumpStart public hub model.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HubAccessConfig) -> dict:
    out: dict = {}
    if "hub_content_arn" in value:
        out["HubContentArn"] = value["hub_content_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> HubAccessConfig:
    out: HubAccessConfig = {}  # type: ignore[typeddict-item]
    if "HubContentArn" in data:
        out["hub_content_arn"] = data["HubContentArn"]
    return out
