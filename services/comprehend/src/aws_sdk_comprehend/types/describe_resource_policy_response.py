"""Generated from Smithy shape ``com.amazonaws.comprehend#DescribeResourcePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.policy
    import aws_sdk_comprehend.types.policy_revision_id
    import aws_sdk_comprehend.types.timestamp


class DescribeResourcePolicyResponse(TypedDict, closed=True):
    resource_policy: NotRequired["aws_sdk_comprehend.types.policy.Policy"]
    """<p>The JSON body of the resource-based policy.</p>"""
    creation_time: NotRequired["aws_sdk_comprehend.types.timestamp.Timestamp"]
    """<p>The time at which the policy was created.</p>"""
    last_modified_time: NotRequired["aws_sdk_comprehend.types.timestamp.Timestamp"]
    """<p>The time at which the policy was last modified.</p>"""
    policy_revision_id: NotRequired[
        "aws_sdk_comprehend.types.policy_revision_id.PolicyRevisionId"
    ]
    """<p>The revision ID of the policy. Each time you modify a policy, Amazon Comprehend assigns a new revision ID, and it deletes the prior version of the policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeResourcePolicyResponse) -> dict:
    out: dict = {}
    if "resource_policy" in value:
        out["ResourcePolicy"] = value["resource_policy"]
    if "creation_time" in value:
        import aws_sdk_comprehend.types.timestamp

        out["CreationTime"] = aws_sdk_comprehend.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import aws_sdk_comprehend.types.timestamp

        out["LastModifiedTime"] = (
            aws_sdk_comprehend.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "policy_revision_id" in value:
        out["PolicyRevisionId"] = value["policy_revision_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeResourcePolicyResponse:
    out: DescribeResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if "ResourcePolicy" in data:
        out["resource_policy"] = data["ResourcePolicy"]
    if "CreationTime" in data:
        import aws_sdk_comprehend.types.timestamp

        out["creation_time"] = (
            aws_sdk_comprehend.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_comprehend.types.timestamp

        out["last_modified_time"] = (
            aws_sdk_comprehend.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "PolicyRevisionId" in data:
        out["policy_revision_id"] = data["PolicyRevisionId"]
    return out
