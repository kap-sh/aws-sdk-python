"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProfilerRuleEvaluationStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.processing_job_arn
    import aws_sdk_sagemaker.types.rule_configuration_name
    import aws_sdk_sagemaker.types.rule_evaluation_status
    import aws_sdk_sagemaker.types.status_details
    import aws_sdk_sagemaker.types.timestamp


class ProfilerRuleEvaluationStatus(TypedDict):
    rule_configuration_name: NotRequired[
        "aws_sdk_sagemaker.types.rule_configuration_name.RuleConfigurationName"
    ]
    """<p>The name of the rule configuration.</p>"""
    rule_evaluation_job_arn: NotRequired[
        "aws_sdk_sagemaker.types.processing_job_arn.ProcessingJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the rule evaluation job.</p>"""
    rule_evaluation_status: NotRequired[
        "aws_sdk_sagemaker.types.rule_evaluation_status.RuleEvaluationStatus"
    ]
    """<p>Status of the rule evaluation.</p>"""
    status_details: NotRequired["aws_sdk_sagemaker.types.status_details.StatusDetails"]
    """<p>Details from the rule evaluation.</p>"""
    last_modified_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>Timestamp when the rule evaluation status was last modified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProfilerRuleEvaluationStatus) -> dict:
    out: dict = {}
    if "rule_configuration_name" in value:
        out["RuleConfigurationName"] = value["rule_configuration_name"]
    if "rule_evaluation_job_arn" in value:
        out["RuleEvaluationJobArn"] = value["rule_evaluation_job_arn"]
    if "rule_evaluation_status" in value:
        import aws_sdk_sagemaker.types.rule_evaluation_status

        out["RuleEvaluationStatus"] = (
            aws_sdk_sagemaker.types.rule_evaluation_status.serialize_aws_json_1_1(
                value["rule_evaluation_status"]
            )
        )
    if "status_details" in value:
        out["StatusDetails"] = value["status_details"]
    if "last_modified_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["LastModifiedTime"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProfilerRuleEvaluationStatus:
    out: ProfilerRuleEvaluationStatus = {}  # type: ignore[typeddict-item]
    if "RuleConfigurationName" in data:
        out["rule_configuration_name"] = data["RuleConfigurationName"]
    if "RuleEvaluationJobArn" in data:
        out["rule_evaluation_job_arn"] = data["RuleEvaluationJobArn"]
    if "RuleEvaluationStatus" in data:
        import aws_sdk_sagemaker.types.rule_evaluation_status

        out["rule_evaluation_status"] = (
            aws_sdk_sagemaker.types.rule_evaluation_status.deserialize_aws_json_1_1(
                data["RuleEvaluationStatus"]
            )
        )
    if "StatusDetails" in data:
        out["status_details"] = data["StatusDetails"]
    if "LastModifiedTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["last_modified_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    return out
