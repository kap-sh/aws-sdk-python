"""Generated from Smithy shape ``com.amazonaws.configservice#ConformancePackEvaluationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.annotation
    import aws_sdk_config_service.types.conformance_pack_compliance_type
    import aws_sdk_config_service.types.date
    import aws_sdk_config_service.types.evaluation_result_identifier


class ConformancePackEvaluationResult(TypedDict, closed=True):
    compliance_type: "aws_sdk_config_service.types.conformance_pack_compliance_type.ConformancePackComplianceType"
    """<p>The compliance type. The allowed values are <code>COMPLIANT</code> and <code>NON_COMPLIANT</code>. <code>INSUFFICIENT_DATA</code> is not supported.</p>"""
    evaluation_result_identifier: "aws_sdk_config_service.types.evaluation_result_identifier.EvaluationResultIdentifier"
    config_rule_invoked_time: "aws_sdk_config_service.types.date.Date"
    """<p>The time when Config rule evaluated Amazon Web Services resource.</p>"""
    result_recorded_time: "aws_sdk_config_service.types.date.Date"
    """<p>The time when Config recorded the evaluation result. </p>"""
    annotation: NotRequired["aws_sdk_config_service.types.annotation.Annotation"]
    """<p>Supplementary information about how the evaluation determined the compliance. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConformancePackEvaluationResult) -> dict:
    out: dict = {}
    import aws_sdk_config_service.types.conformance_pack_compliance_type

    out["ComplianceType"] = (
        aws_sdk_config_service.types.conformance_pack_compliance_type.serialize_aws_json_1_1(
            value["compliance_type"]
        )
    )
    import aws_sdk_config_service.types.evaluation_result_identifier

    out["EvaluationResultIdentifier"] = (
        aws_sdk_config_service.types.evaluation_result_identifier.serialize_aws_json_1_1(
            value["evaluation_result_identifier"]
        )
    )
    import aws_sdk_config_service.types.date

    out["ConfigRuleInvokedTime"] = (
        aws_sdk_config_service.types.date.serialize_aws_json_1_1(
            value["config_rule_invoked_time"]
        )
    )
    import aws_sdk_config_service.types.date

    out["ResultRecordedTime"] = (
        aws_sdk_config_service.types.date.serialize_aws_json_1_1(
            value["result_recorded_time"]
        )
    )
    if "annotation" in value:
        out["Annotation"] = value["annotation"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConformancePackEvaluationResult:
    out: ConformancePackEvaluationResult = {}  # type: ignore[typeddict-item]
    if "ComplianceType" in data:
        import aws_sdk_config_service.types.conformance_pack_compliance_type

        out["compliance_type"] = (
            aws_sdk_config_service.types.conformance_pack_compliance_type.deserialize_aws_json_1_1(
                data["ComplianceType"]
            )
        )
    else:
        raise DeserializationError(
            "ConformancePackEvaluationResult.compliance_type required"
        )
    if "EvaluationResultIdentifier" in data:
        import aws_sdk_config_service.types.evaluation_result_identifier

        out["evaluation_result_identifier"] = (
            aws_sdk_config_service.types.evaluation_result_identifier.deserialize_aws_json_1_1(
                data["EvaluationResultIdentifier"]
            )
        )
    else:
        raise DeserializationError(
            "ConformancePackEvaluationResult.evaluation_result_identifier required"
        )
    if "ConfigRuleInvokedTime" in data:
        import aws_sdk_config_service.types.date

        out["config_rule_invoked_time"] = (
            aws_sdk_config_service.types.date.deserialize_aws_json_1_1(
                data["ConfigRuleInvokedTime"]
            )
        )
    else:
        raise DeserializationError(
            "ConformancePackEvaluationResult.config_rule_invoked_time required"
        )
    if "ResultRecordedTime" in data:
        import aws_sdk_config_service.types.date

        out["result_recorded_time"] = (
            aws_sdk_config_service.types.date.deserialize_aws_json_1_1(
                data["ResultRecordedTime"]
            )
        )
    else:
        raise DeserializationError(
            "ConformancePackEvaluationResult.result_recorded_time required"
        )
    if "Annotation" in data:
        out["annotation"] = data["Annotation"]
    return out
