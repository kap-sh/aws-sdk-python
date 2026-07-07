"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#IndexPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.index_source
    import aws_sdk_cloudwatch_logs.types.log_group_identifier
    import aws_sdk_cloudwatch_logs.types.policy_document
    import aws_sdk_cloudwatch_logs.types.policy_name
    import aws_sdk_cloudwatch_logs.types.timestamp


class IndexPolicy(TypedDict, closed=True):
    log_group_identifier: NotRequired[
        "aws_sdk_cloudwatch_logs.types.log_group_identifier.LogGroupIdentifier"
    ]
    """<p>The ARN of the log group that this index policy applies to.</p>"""
    last_update_time: NotRequired["aws_sdk_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The date and time that this index policy was most recently updated.</p>"""
    policy_document: NotRequired[
        "aws_sdk_cloudwatch_logs.types.policy_document.PolicyDocument"
    ]
    """<p>The policy document for this index policy, in JSON format.</p>"""
    policy_name: NotRequired["aws_sdk_cloudwatch_logs.types.policy_name.PolicyName"]
    """<p>The name of this policy. Responses about log group-level field index policies don't have this field, because those policies don't have names.</p>"""
    source: NotRequired["aws_sdk_cloudwatch_logs.types.index_source.IndexSource"]
    """<p>This field indicates whether this is an account-level index policy or an index policy that applies only to a single log group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IndexPolicy) -> dict:
    out: dict = {}
    if "log_group_identifier" in value:
        out["logGroupIdentifier"] = value["log_group_identifier"]
    if "last_update_time" in value:
        out["lastUpdateTime"] = value["last_update_time"]
    if "policy_document" in value:
        out["policyDocument"] = value["policy_document"]
    if "policy_name" in value:
        out["policyName"] = value["policy_name"]
    if "source" in value:
        import aws_sdk_cloudwatch_logs.types.index_source

        out["source"] = (
            aws_sdk_cloudwatch_logs.types.index_source.serialize_aws_json_1_1(
                value["source"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> IndexPolicy:
    out: IndexPolicy = {}  # type: ignore[typeddict-item]
    if "logGroupIdentifier" in data:
        out["log_group_identifier"] = data["logGroupIdentifier"]
    if "lastUpdateTime" in data:
        out["last_update_time"] = data["lastUpdateTime"]
    if "policyDocument" in data:
        out["policy_document"] = data["policyDocument"]
    if "policyName" in data:
        out["policy_name"] = data["policyName"]
    if "source" in data:
        import aws_sdk_cloudwatch_logs.types.index_source

        out["source"] = (
            aws_sdk_cloudwatch_logs.types.index_source.deserialize_aws_json_1_1(
                data["source"]
            )
        )
    return out
