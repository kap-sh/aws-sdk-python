"""Generated from Smithy shape ``com.amazonaws.mpa#GetResourcePolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mpa.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mpa.types.policy_type
    import aws_sdk_mpa.types.string


class GetResourcePolicyRequest(TypedDict):
    resource_arn: "aws_sdk_mpa.types.string.String"
    """<p>Amazon Resource Name (ARN) for the resource.</p>"""
    policy_name: "aws_sdk_mpa.types.string.String"
    """<p>Name of the policy.</p>"""
    policy_type: "aws_sdk_mpa.types.policy_type.PolicyType"
    """<p>The type of policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourcePolicyRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    out["PolicyName"] = value["policy_name"]
    import aws_sdk_mpa.types.policy_type

    out["PolicyType"] = aws_sdk_mpa.types.policy_type.serialize_json(
        value["policy_type"]
    )
    return out


def deserialize_json(data: dict) -> GetResourcePolicyRequest:
    out: GetResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("GetResourcePolicyRequest.resource_arn required")
    if "PolicyName" in data:
        out["policy_name"] = data["PolicyName"]
    else:
        raise DeserializationError("GetResourcePolicyRequest.policy_name required")
    if "PolicyType" in data:
        import aws_sdk_mpa.types.policy_type

        out["policy_type"] = aws_sdk_mpa.types.policy_type.deserialize_json(
            data["PolicyType"]
        )
    else:
        raise DeserializationError("GetResourcePolicyRequest.policy_type required")
    return out
