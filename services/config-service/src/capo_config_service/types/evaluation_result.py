"""Generated from Smithy shape ``com.amazonaws.configservice#EvaluationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.compliance_type
    import capo_config_service.types.date
    import capo_config_service.types.evaluation_result_identifier
    import capo_config_service.types.string
    import capo_config_service.types.string_with_char_limit256


class EvaluationResult(TypedDict, closed=True):
    evaluation_result_identifier: NotRequired[
        "capo_config_service.types.evaluation_result_identifier.EvaluationResultIdentifier"
    ]
    """<p>Uniquely identifies the evaluation result.</p>"""
    compliance_type: NotRequired[
        "capo_config_service.types.compliance_type.ComplianceType"
    ]
    """<p>Indicates whether the Amazon Web Services resource complies with the Config rule that evaluated it.</p> <p>For the <code>EvaluationResult</code> data type, Config supports only the <code>COMPLIANT</code>, <code>NON_COMPLIANT</code>, and <code>NOT_APPLICABLE</code> values. Config does not support the <code>INSUFFICIENT_DATA</code> value for the <code>EvaluationResult</code> data type.</p>"""
    result_recorded_time: NotRequired["capo_config_service.types.date.Date"]
    """<p>The time when Config recorded the evaluation result.</p>"""
    config_rule_invoked_time: NotRequired["capo_config_service.types.date.Date"]
    """<p>The time when the Config rule evaluated the Amazon Web Services resource.</p>"""
    annotation: NotRequired[
        "capo_config_service.types.string_with_char_limit256.StringWithCharLimit256"
    ]
    """<p>Supplementary information about how the evaluation determined the compliance.</p>"""
    result_token: NotRequired["capo_config_service.types.string.String"]
    """<p>An encrypted token that associates an evaluation with an Config rule. The token identifies the rule, the Amazon Web Services resource being evaluated, and the event that triggered the evaluation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EvaluationResult) -> dict:
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
    if "result_token" in value:
        out["ResultToken"] = value["result_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EvaluationResult:
    out: EvaluationResult = {}  # type: ignore[typeddict-item]
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
    if "ResultToken" in data:
        out["result_token"] = data["ResultToken"]
    return out
