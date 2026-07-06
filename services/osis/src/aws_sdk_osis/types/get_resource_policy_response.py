"""Generated from Smithy shape ``com.amazonaws.osis#GetResourcePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_osis.types.pipeline_arn
    import aws_sdk_osis.types.resource_policy


class GetResourcePolicyResponse(TypedDict, closed=True):
    resource_arn: NotRequired["aws_sdk_osis.types.pipeline_arn.PipelineArn"]
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    policy: NotRequired["aws_sdk_osis.types.resource_policy.ResourcePolicy"]
    """<p>The resource-based policy document in JSON format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourcePolicyResponse) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "policy" in value:
        out["Policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> GetResourcePolicyResponse:
    out: GetResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "Policy" in data:
        out["policy"] = data["Policy"]
    return out
