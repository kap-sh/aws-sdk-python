"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ResourcePolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.arn
    import capo_cloudwatch_logs.types.expected_revision_id
    import capo_cloudwatch_logs.types.policy_document
    import capo_cloudwatch_logs.types.policy_name
    import capo_cloudwatch_logs.types.policy_scope
    import capo_cloudwatch_logs.types.timestamp


class ResourcePolicy(TypedDict, closed=True):
    policy_name: NotRequired["capo_cloudwatch_logs.types.policy_name.PolicyName"]
    """<p>The name of the resource policy.</p>"""
    policy_document: NotRequired[
        "capo_cloudwatch_logs.types.policy_document.PolicyDocument"
    ]
    """<p>The details of the policy.</p>"""
    last_updated_time: NotRequired["capo_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>Timestamp showing when this policy was last updated, expressed as the number of milliseconds after <code>Jan 1, 1970 00:00:00 UTC</code>.</p>"""
    policy_scope: NotRequired["capo_cloudwatch_logs.types.policy_scope.PolicyScope"]
    """<p>Specifies scope of the resource policy. Valid values are ACCOUNT or RESOURCE.</p>"""
    resource_arn: NotRequired["capo_cloudwatch_logs.types.arn.Arn"]
    """<p>The ARN of the CloudWatch Logs resource to which the resource policy is attached. Only populated for resource-scoped policies.</p>"""
    revision_id: NotRequired[
        "capo_cloudwatch_logs.types.expected_revision_id.ExpectedRevisionId"
    ]
    """<p>The revision ID of the resource policy. Only populated for resource-scoped policies.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourcePolicy) -> dict:
    out: dict = {}
    if "policy_name" in value:
        out["policyName"] = value["policy_name"]
    if "policy_document" in value:
        out["policyDocument"] = value["policy_document"]
    if "last_updated_time" in value:
        out["lastUpdatedTime"] = value["last_updated_time"]
    if "policy_scope" in value:
        import capo_cloudwatch_logs.types.policy_scope

        out["policyScope"] = (
            capo_cloudwatch_logs.types.policy_scope.serialize_aws_json_1_1(
                value["policy_scope"]
            )
        )
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    if "revision_id" in value:
        out["revisionId"] = value["revision_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourcePolicy:
    out: ResourcePolicy = {}  # type: ignore[typeddict-item]
    if "policyName" in data:
        out["policy_name"] = data["policyName"]
    if "policyDocument" in data:
        out["policy_document"] = data["policyDocument"]
    if "lastUpdatedTime" in data:
        out["last_updated_time"] = data["lastUpdatedTime"]
    if "policyScope" in data:
        import capo_cloudwatch_logs.types.policy_scope

        out["policy_scope"] = (
            capo_cloudwatch_logs.types.policy_scope.deserialize_aws_json_1_1(
                data["policyScope"]
            )
        )
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    if "revisionId" in data:
        out["revision_id"] = data["revisionId"]
    return out
