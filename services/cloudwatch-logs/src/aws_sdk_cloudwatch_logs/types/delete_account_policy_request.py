"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DeleteAccountPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.policy_name
    import aws_sdk_cloudwatch_logs.types.policy_type


class DeleteAccountPolicyRequest(TypedDict, closed=True):
    policy_name: "aws_sdk_cloudwatch_logs.types.policy_name.PolicyName"
    """<p>The name of the policy to delete.</p>"""
    policy_type: "aws_sdk_cloudwatch_logs.types.policy_type.PolicyType"
    """<p>The type of policy to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAccountPolicyRequest) -> dict:
    out: dict = {}
    out["policyName"] = value["policy_name"]
    import aws_sdk_cloudwatch_logs.types.policy_type

    out["policyType"] = (
        aws_sdk_cloudwatch_logs.types.policy_type.serialize_aws_json_1_1(
            value["policy_type"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAccountPolicyRequest:
    out: DeleteAccountPolicyRequest = {}  # type: ignore[typeddict-item]
    if "policyName" in data:
        out["policy_name"] = data["policyName"]
    else:
        raise DeserializationError("DeleteAccountPolicyRequest.policy_name required")
    if "policyType" in data:
        import aws_sdk_cloudwatch_logs.types.policy_type

        out["policy_type"] = (
            aws_sdk_cloudwatch_logs.types.policy_type.deserialize_aws_json_1_1(
                data["policyType"]
            )
        )
    else:
        raise DeserializationError("DeleteAccountPolicyRequest.policy_type required")
    return out
