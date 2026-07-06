"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#PutResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lookoutequipment.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.idempotence_token
    import aws_sdk_lookoutequipment.types.policy
    import aws_sdk_lookoutequipment.types.policy_revision_id
    import aws_sdk_lookoutequipment.types.resource_arn


class PutResourcePolicyRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_lookoutequipment.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource for which the policy is being created.</p>"""
    resource_policy: "aws_sdk_lookoutequipment.types.policy.Policy"
    """<p>The JSON-formatted resource policy to create.</p>"""
    policy_revision_id: NotRequired[
        "aws_sdk_lookoutequipment.types.policy_revision_id.PolicyRevisionId"
    ]
    """<p>A unique identifier for a revision of the resource policy.</p>"""
    client_token: "aws_sdk_lookoutequipment.types.idempotence_token.IdempotenceToken"
    """<p>A unique identifier for the request. If you do not set the client request token, Amazon Lookout for Equipment generates one. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutResourcePolicyRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    out["ResourcePolicy"] = value["resource_policy"]
    if "policy_revision_id" in value:
        out["PolicyRevisionId"] = value["policy_revision_id"]
    out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PutResourcePolicyRequest:
    out: PutResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("PutResourcePolicyRequest.resource_arn required")
    if "ResourcePolicy" in data:
        out["resource_policy"] = data["ResourcePolicy"]
    else:
        raise DeserializationError("PutResourcePolicyRequest.resource_policy required")
    if "PolicyRevisionId" in data:
        out["policy_revision_id"] = data["PolicyRevisionId"]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    else:
        raise DeserializationError("PutResourcePolicyRequest.client_token required")
    return out
