"""Generated from Smithy shape ``com.amazonaws.fms#PutPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fms.types.policy
    import aws_sdk_fms.types.resource_arn


class PutPolicyResponse(TypedDict, closed=True):
    policy: NotRequired["aws_sdk_fms.types.policy.Policy"]
    """<p>The details of the Firewall Manager policy.</p>"""
    policy_arn: NotRequired["aws_sdk_fms.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutPolicyResponse) -> dict:
    out: dict = {}
    if "policy" in value:
        import aws_sdk_fms.types.policy

        out["Policy"] = aws_sdk_fms.types.policy.serialize_aws_json_1_1(value["policy"])
    if "policy_arn" in value:
        out["PolicyArn"] = value["policy_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutPolicyResponse:
    out: PutPolicyResponse = {}  # type: ignore[typeddict-item]
    if "Policy" in data:
        import aws_sdk_fms.types.policy

        out["policy"] = aws_sdk_fms.types.policy.deserialize_aws_json_1_1(
            data["Policy"]
        )
    if "PolicyArn" in data:
        out["policy_arn"] = data["PolicyArn"]
    return out
