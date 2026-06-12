"""Generated from Smithy shape ``com.amazonaws.fms#GetPolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fms.types.policy
    import aws_sdk_fms.types.resource_arn


class GetPolicyResponse(TypedDict):
    policy: NotRequired["aws_sdk_fms.types.policy.Policy"]
    """<p>Information about the specified Firewall Manager policy.</p>"""
    policy_arn: NotRequired["aws_sdk_fms.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the specified policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPolicyResponse) -> dict:
    out: dict = {}
    if "policy" in value:
        import aws_sdk_fms.types.policy

        out["Policy"] = aws_sdk_fms.types.policy.serialize_aws_json_1_1(value["policy"])
    if "policy_arn" in value:
        out["PolicyArn"] = value["policy_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPolicyResponse:
    out: GetPolicyResponse = {}  # type: ignore[typeddict-item]
    if "Policy" in data:
        import aws_sdk_fms.types.policy

        out["policy"] = aws_sdk_fms.types.policy.deserialize_aws_json_1_1(
            data["Policy"]
        )
    if "PolicyArn" in data:
        out["policy_arn"] = data["PolicyArn"]
    return out
