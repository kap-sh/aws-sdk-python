"""Generated from Smithy shape ``com.amazonaws.organizations#EffectivePolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_organizations.types.effective_policy_type
    import aws_sdk_organizations.types.policy_content
    import aws_sdk_organizations.types.policy_target_id
    import aws_sdk_organizations.types.timestamp


class EffectivePolicy(TypedDict, closed=True):
    policy_content: NotRequired[
        "aws_sdk_organizations.types.policy_content.PolicyContent"
    ]
    """<p>The text content of the policy.</p>"""
    last_updated_timestamp: NotRequired[
        "aws_sdk_organizations.types.timestamp.Timestamp"
    ]
    """<p>The time of the last update to this policy.</p>"""
    target_id: NotRequired[
        "aws_sdk_organizations.types.policy_target_id.PolicyTargetId"
    ]
    """<p>The account ID of the policy target. </p>"""
    policy_type: NotRequired[
        "aws_sdk_organizations.types.effective_policy_type.EffectivePolicyType"
    ]
    """<p>The policy type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EffectivePolicy) -> dict:
    out: dict = {}
    if "policy_content" in value:
        out["PolicyContent"] = value["policy_content"]
    if "last_updated_timestamp" in value:
        import aws_sdk_organizations.types.timestamp

        out["LastUpdatedTimestamp"] = (
            aws_sdk_organizations.types.timestamp.serialize_aws_json_1_1(
                value["last_updated_timestamp"]
            )
        )
    if "target_id" in value:
        out["TargetId"] = value["target_id"]
    if "policy_type" in value:
        import aws_sdk_organizations.types.effective_policy_type

        out["PolicyType"] = (
            aws_sdk_organizations.types.effective_policy_type.serialize_aws_json_1_1(
                value["policy_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EffectivePolicy:
    out: EffectivePolicy = {}  # type: ignore[typeddict-item]
    if "PolicyContent" in data:
        out["policy_content"] = data["PolicyContent"]
    if "LastUpdatedTimestamp" in data:
        import aws_sdk_organizations.types.timestamp

        out["last_updated_timestamp"] = (
            aws_sdk_organizations.types.timestamp.deserialize_aws_json_1_1(
                data["LastUpdatedTimestamp"]
            )
        )
    if "TargetId" in data:
        out["target_id"] = data["TargetId"]
    if "PolicyType" in data:
        import aws_sdk_organizations.types.effective_policy_type

        out["policy_type"] = (
            aws_sdk_organizations.types.effective_policy_type.deserialize_aws_json_1_1(
                data["PolicyType"]
            )
        )
    return out
