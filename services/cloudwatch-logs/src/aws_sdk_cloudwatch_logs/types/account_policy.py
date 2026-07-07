"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#AccountPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.account_id
    import aws_sdk_cloudwatch_logs.types.account_policy_document
    import aws_sdk_cloudwatch_logs.types.policy_name
    import aws_sdk_cloudwatch_logs.types.policy_type
    import aws_sdk_cloudwatch_logs.types.scope
    import aws_sdk_cloudwatch_logs.types.selection_criteria
    import aws_sdk_cloudwatch_logs.types.timestamp


class AccountPolicy(TypedDict, closed=True):
    policy_name: NotRequired["aws_sdk_cloudwatch_logs.types.policy_name.PolicyName"]
    """<p>The name of the account policy.</p>"""
    policy_document: NotRequired[
        "aws_sdk_cloudwatch_logs.types.account_policy_document.AccountPolicyDocument"
    ]
    """<p>The policy document for this account policy.</p> <p>The JSON specified in <code>policyDocument</code> can be up to 30,720 characters.</p>"""
    last_updated_time: NotRequired["aws_sdk_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The date and time that this policy was most recently updated.</p>"""
    policy_type: NotRequired["aws_sdk_cloudwatch_logs.types.policy_type.PolicyType"]
    """<p>The type of policy for this account policy.</p>"""
    scope: NotRequired["aws_sdk_cloudwatch_logs.types.scope.Scope"]
    """<p>The scope of the account policy.</p>"""
    selection_criteria: NotRequired[
        "aws_sdk_cloudwatch_logs.types.selection_criteria.SelectionCriteria"
    ]
    """<p>The log group selection criteria that is used for this policy.</p>"""
    account_id: NotRequired["aws_sdk_cloudwatch_logs.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID that the policy applies to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountPolicy) -> dict:
    out: dict = {}
    if "policy_name" in value:
        out["policyName"] = value["policy_name"]
    if "policy_document" in value:
        out["policyDocument"] = value["policy_document"]
    if "last_updated_time" in value:
        out["lastUpdatedTime"] = value["last_updated_time"]
    if "policy_type" in value:
        import aws_sdk_cloudwatch_logs.types.policy_type

        out["policyType"] = (
            aws_sdk_cloudwatch_logs.types.policy_type.serialize_aws_json_1_1(
                value["policy_type"]
            )
        )
    if "scope" in value:
        import aws_sdk_cloudwatch_logs.types.scope

        out["scope"] = aws_sdk_cloudwatch_logs.types.scope.serialize_aws_json_1_1(
            value["scope"]
        )
    if "selection_criteria" in value:
        out["selectionCriteria"] = value["selection_criteria"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AccountPolicy:
    out: AccountPolicy = {}  # type: ignore[typeddict-item]
    if "policyName" in data:
        out["policy_name"] = data["policyName"]
    if "policyDocument" in data:
        out["policy_document"] = data["policyDocument"]
    if "lastUpdatedTime" in data:
        out["last_updated_time"] = data["lastUpdatedTime"]
    if "policyType" in data:
        import aws_sdk_cloudwatch_logs.types.policy_type

        out["policy_type"] = (
            aws_sdk_cloudwatch_logs.types.policy_type.deserialize_aws_json_1_1(
                data["policyType"]
            )
        )
    if "scope" in data:
        import aws_sdk_cloudwatch_logs.types.scope

        out["scope"] = aws_sdk_cloudwatch_logs.types.scope.deserialize_aws_json_1_1(
            data["scope"]
        )
    if "selectionCriteria" in data:
        out["selection_criteria"] = data["selectionCriteria"]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    return out
