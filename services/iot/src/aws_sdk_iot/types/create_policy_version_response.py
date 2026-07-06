"""Generated from Smithy shape ``com.amazonaws.iot#CreatePolicyVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.is_default_version
    import aws_sdk_iot.types.policy_arn
    import aws_sdk_iot.types.policy_document
    import aws_sdk_iot.types.policy_version_id


class CreatePolicyVersionResponse(TypedDict, closed=True):
    policy_arn: NotRequired["aws_sdk_iot.types.policy_arn.PolicyArn"]
    """<p>The policy ARN.</p>"""
    policy_document: NotRequired["aws_sdk_iot.types.policy_document.PolicyDocument"]
    """<p>The JSON document that describes the policy.</p>"""
    policy_version_id: NotRequired[
        "aws_sdk_iot.types.policy_version_id.PolicyVersionId"
    ]
    """<p>The policy version ID.</p>"""
    is_default_version: "aws_sdk_iot.types.is_default_version.IsDefaultVersion"
    """<p>Specifies whether the policy version is the default.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePolicyVersionResponse) -> dict:
    out: dict = {}
    if "policy_arn" in value:
        out["policyArn"] = value["policy_arn"]
    if "policy_document" in value:
        out["policyDocument"] = value["policy_document"]
    if "policy_version_id" in value:
        out["policyVersionId"] = value["policy_version_id"]
    out["isDefaultVersion"] = value.get("is_default_version", False)
    return out


def deserialize_json(data: dict) -> CreatePolicyVersionResponse:
    out: CreatePolicyVersionResponse = {}  # type: ignore[typeddict-item]
    if "policyArn" in data:
        out["policy_arn"] = data["policyArn"]
    if "policyDocument" in data:
        out["policy_document"] = data["policyDocument"]
    if "policyVersionId" in data:
        out["policy_version_id"] = data["policyVersionId"]
    if "isDefaultVersion" in data:
        out["is_default_version"] = data["isDefaultVersion"]
    else:
        out["is_default_version"] = False
    return out
