"""Generated from Smithy shape ``com.amazonaws.configservice#AggregateEvaluationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.account_id
    import capo_config_service.types.aws_region
    import capo_config_service.types.compliance_type
    import capo_config_service.types.date
    import capo_config_service.types.evaluation_result_identifier
    import capo_config_service.types.string_with_char_limit256


class AggregateEvaluationResult(TypedDict, closed=True):
    evaluation_result_identifier: NotRequired[
        "capo_config_service.types.evaluation_result_identifier.EvaluationResultIdentifier"
    ]
    """<p>Uniquely identifies the evaluation result.</p>"""
    compliance_type: NotRequired[
        "capo_config_service.types.compliance_type.ComplianceType"
    ]
    """<p>The resource compliance status.</p> <p>For the <code>AggregationEvaluationResult</code> data type, Config supports only the <code>COMPLIANT</code> and <code>NON_COMPLIANT</code>. Config does not support the <code>NOT_APPLICABLE</code> and <code>INSUFFICIENT_DATA</code> value.</p>"""
    result_recorded_time: NotRequired["capo_config_service.types.date.Date"]
    """<p>The time when Config recorded the aggregate evaluation result.</p>"""
    config_rule_invoked_time: NotRequired["capo_config_service.types.date.Date"]
    """<p>The time when the Config rule evaluated the Amazon Web Services resource.</p>"""
    annotation: NotRequired[
        "capo_config_service.types.string_with_char_limit256.StringWithCharLimit256"
    ]
    """<p>Supplementary information about how the agrregate evaluation determined the compliance.</p>"""
    account_id: NotRequired["capo_config_service.types.account_id.AccountId"]
    """<p>The 12-digit account ID of the source account.</p>"""
    aws_region: NotRequired["capo_config_service.types.aws_region.AwsRegion"]
    """<p>The source region from where the data is aggregated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AggregateEvaluationResult) -> dict:
    out: dict = {}
    if "evaluation_result_identifier" in value:
        import capo_config_service.types.evaluation_result_identifier

        out["EvaluationResultIdentifier"] = (
            capo_config_service.types.evaluation_result_identifier.serialize_aws_json_1_1(
                value["evaluation_result_identifier"]
            )
        )
    if "compliance_type" in value:
        import capo_config_service.types.compliance_type

        out["ComplianceType"] = (
            capo_config_service.types.compliance_type.serialize_aws_json_1_1(
                value["compliance_type"]
            )
        )
    if "result_recorded_time" in value:
        import capo_config_service.types.date

        out["ResultRecordedTime"] = (
            capo_config_service.types.date.serialize_aws_json_1_1(
                value["result_recorded_time"]
            )
        )
    if "config_rule_invoked_time" in value:
        import capo_config_service.types.date

        out["ConfigRuleInvokedTime"] = (
            capo_config_service.types.date.serialize_aws_json_1_1(
                value["config_rule_invoked_time"]
            )
        )
    if "annotation" in value:
        out["Annotation"] = value["annotation"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "aws_region" in value:
        out["AwsRegion"] = value["aws_region"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AggregateEvaluationResult:
    out: AggregateEvaluationResult = {}  # type: ignore[typeddict-item]
    if "EvaluationResultIdentifier" in data:
        import capo_config_service.types.evaluation_result_identifier

        out["evaluation_result_identifier"] = (
            capo_config_service.types.evaluation_result_identifier.deserialize_aws_json_1_1(
                data["EvaluationResultIdentifier"]
            )
        )
    if "ComplianceType" in data:
        import capo_config_service.types.compliance_type

        out["compliance_type"] = (
            capo_config_service.types.compliance_type.deserialize_aws_json_1_1(
                data["ComplianceType"]
            )
        )
    if "ResultRecordedTime" in data:
        import capo_config_service.types.date

        out["result_recorded_time"] = (
            capo_config_service.types.date.deserialize_aws_json_1_1(
                data["ResultRecordedTime"]
            )
        )
    if "ConfigRuleInvokedTime" in data:
        import capo_config_service.types.date

        out["config_rule_invoked_time"] = (
            capo_config_service.types.date.deserialize_aws_json_1_1(
                data["ConfigRuleInvokedTime"]
            )
        )
    if "Annotation" in data:
        out["annotation"] = data["Annotation"]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "AwsRegion" in data:
        out["aws_region"] = data["AwsRegion"]
    return out
