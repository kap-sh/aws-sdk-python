"""Generated from Smithy shape ``com.amazonaws.osis#PutResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_osis.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_osis.types.pipeline_arn
    import aws_sdk_osis.types.resource_policy


class PutResourcePolicyRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_osis.types.pipeline_arn.PipelineArn"
    """<p>The Amazon Resource Name (ARN) of the resource to attach the policy to.</p>"""
    policy: "aws_sdk_osis.types.resource_policy.ResourcePolicy"
    """<p>The resource-based policy document in JSON format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutResourcePolicyRequest) -> dict:
    out: dict = {}
    out["Policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> PutResourcePolicyRequest:
    out: PutResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    if "Policy" in data:
        out["policy"] = data["Policy"]
    else:
        raise DeserializationError("PutResourcePolicyRequest.policy required")
    return out
