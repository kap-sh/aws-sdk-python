"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#PutResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_migration_hub_refactor_spaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_migration_hub_refactor_spaces.types.policy_string
    import aws_sdk_migration_hub_refactor_spaces.types.resource_arn


class PutResourcePolicyRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_migration_hub_refactor_spaces.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource to which the policy is being attached. </p>"""
    policy: "aws_sdk_migration_hub_refactor_spaces.types.policy_string.PolicyString"
    """<p>A JSON-formatted string for an Amazon Web Services resource-based policy. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutResourcePolicyRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    out["Policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> PutResourcePolicyRequest:
    out: PutResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("PutResourcePolicyRequest.resource_arn required")
    if "Policy" in data:
        out["policy"] = data["Policy"]
    else:
        raise DeserializationError("PutResourcePolicyRequest.policy required")
    return out
