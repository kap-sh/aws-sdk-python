"""Generated from Smithy shape ``com.amazonaws.entityresolution#DeletePolicyStatementOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_entityresolution.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.policy_document
    import aws_sdk_entityresolution.types.policy_token
    import aws_sdk_entityresolution.types.venice_global_arn


class DeletePolicyStatementOutput(TypedDict):
    arn: "aws_sdk_entityresolution.types.venice_global_arn.VeniceGlobalArn"
    """<p>The ARN of the resource for which the policy need to be deleted.</p>"""
    token: "aws_sdk_entityresolution.types.policy_token.PolicyToken"
    """<p>A unique identifier for the deleted policy.</p>"""
    policy: NotRequired["aws_sdk_entityresolution.types.policy_document.PolicyDocument"]
    """<p>The resource-based policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePolicyStatementOutput) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["token"] = value["token"]
    if "policy" in value:
        out["policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> DeletePolicyStatementOutput:
    out: DeletePolicyStatementOutput = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("DeletePolicyStatementOutput.arn required")
    if "token" in data:
        out["token"] = data["token"]
    else:
        raise DeserializationError("DeletePolicyStatementOutput.token required")
    if "policy" in data:
        out["policy"] = data["policy"]
    return out
