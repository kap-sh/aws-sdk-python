"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceHubAccessConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.hub_content_arn


class InferenceHubAccessConfig(TypedDict, closed=True):
    hub_content_arn: NotRequired["capo_sagemaker.types.hub_content_arn.HubContentArn"]
    """<p>The ARN of the hub content for which deployment access is allowed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferenceHubAccessConfig) -> dict:
    out: dict = {}
    if "hub_content_arn" in value:
        out["HubContentArn"] = value["hub_content_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InferenceHubAccessConfig:
    out: InferenceHubAccessConfig = {}  # type: ignore[typeddict-item]
    if "HubContentArn" in data:
        out["hub_content_arn"] = data["HubContentArn"]
    return out
