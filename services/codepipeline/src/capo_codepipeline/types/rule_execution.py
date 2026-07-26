"""Generated from Smithy shape ``com.amazonaws.codepipeline#RuleExecution``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.error_details
    import capo_codepipeline.types.execution_id
    import capo_codepipeline.types.execution_summary
    import capo_codepipeline.types.last_updated_by
    import capo_codepipeline.types.rule_execution_id
    import capo_codepipeline.types.rule_execution_status
    import capo_codepipeline.types.rule_execution_token
    import capo_codepipeline.types.timestamp
    import capo_codepipeline.types.url


class RuleExecution(TypedDict, closed=True):
    rule_execution_id: NotRequired[
        "capo_codepipeline.types.rule_execution_id.RuleExecutionId"
    ]
    """<p>The execution ID for the run of the rule.</p>"""
    status: NotRequired[
        "capo_codepipeline.types.rule_execution_status.RuleExecutionStatus"
    ]
    """<p>The status of the run of the rule, such as FAILED.</p>"""
    summary: NotRequired["capo_codepipeline.types.execution_summary.ExecutionSummary"]
    """<p>A summary of the run of the rule.</p>"""
    last_status_change: NotRequired["capo_codepipeline.types.timestamp.Timestamp"]
    """<p>The last status change of the rule.</p>"""
    token: NotRequired[
        "capo_codepipeline.types.rule_execution_token.RuleExecutionToken"
    ]
    """<p>The system-generated token used to identify a unique request.</p>"""
    last_updated_by: NotRequired[
        "capo_codepipeline.types.last_updated_by.LastUpdatedBy"
    ]
    """<p>The ARN of the user who last changed the rule.</p>"""
    external_execution_id: NotRequired[
        "capo_codepipeline.types.execution_id.ExecutionId"
    ]
    """<p>The external ID of the run of the rule.</p>"""
    external_execution_url: NotRequired["capo_codepipeline.types.url.Url"]
    """<p>The URL of a resource external to Amazon Web Services that is used when running the rule (for example, an external repository URL).</p>"""
    error_details: NotRequired["capo_codepipeline.types.error_details.ErrorDetails"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleExecution) -> dict:
    out: dict = {}
    if "rule_execution_id" in value:
        out["ruleExecutionId"] = value["rule_execution_id"]
    if "status" in value:
        import capo_codepipeline.types.rule_execution_status

        out["status"] = (
            capo_codepipeline.types.rule_execution_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "summary" in value:
        out["summary"] = value["summary"]
    if "last_status_change" in value:
        import capo_codepipeline.types.timestamp

        out["lastStatusChange"] = (
            capo_codepipeline.types.timestamp.serialize_aws_json_1_1(
                value["last_status_change"]
            )
        )
    if "token" in value:
        out["token"] = value["token"]
    if "last_updated_by" in value:
        out["lastUpdatedBy"] = value["last_updated_by"]
    if "external_execution_id" in value:
        out["externalExecutionId"] = value["external_execution_id"]
    if "external_execution_url" in value:
        out["externalExecutionUrl"] = value["external_execution_url"]
    if "error_details" in value:
        import capo_codepipeline.types.error_details

        out["errorDetails"] = (
            capo_codepipeline.types.error_details.serialize_aws_json_1_1(
                value["error_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RuleExecution:
    out: RuleExecution = {}  # type: ignore[typeddict-item]
    if "ruleExecutionId" in data:
        out["rule_execution_id"] = data["ruleExecutionId"]
    if "status" in data:
        import capo_codepipeline.types.rule_execution_status

        out["status"] = (
            capo_codepipeline.types.rule_execution_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "summary" in data:
        out["summary"] = data["summary"]
    if "lastStatusChange" in data:
        import capo_codepipeline.types.timestamp

        out["last_status_change"] = (
            capo_codepipeline.types.timestamp.deserialize_aws_json_1_1(
                data["lastStatusChange"]
            )
        )
    if "token" in data:
        out["token"] = data["token"]
    if "lastUpdatedBy" in data:
        out["last_updated_by"] = data["lastUpdatedBy"]
    if "externalExecutionId" in data:
        out["external_execution_id"] = data["externalExecutionId"]
    if "externalExecutionUrl" in data:
        out["external_execution_url"] = data["externalExecutionUrl"]
    if "errorDetails" in data:
        import capo_codepipeline.types.error_details

        out["error_details"] = (
            capo_codepipeline.types.error_details.deserialize_aws_json_1_1(
                data["errorDetails"]
            )
        )
    return out
