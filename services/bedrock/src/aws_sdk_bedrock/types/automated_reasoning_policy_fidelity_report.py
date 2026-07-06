"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyFidelityReport``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_accuracy_score
    import aws_sdk_bedrock.types.automated_reasoning_policy_coverage_score
    import aws_sdk_bedrock.types.automated_reasoning_policy_report_source_document_list
    import aws_sdk_bedrock.types.automated_reasoning_policy_rule_report_map
    import aws_sdk_bedrock.types.automated_reasoning_policy_variable_report_map


class AutomatedReasoningPolicyFidelityReport(TypedDict, closed=True):
    coverage_score: "aws_sdk_bedrock.types.automated_reasoning_policy_coverage_score.AutomatedReasoningPolicyCoverageScore"
    """<p>A score from 0.0 to 1.0 indicating how well the policy covers the statements in the source documents. A higher score means more of the source content is represented in the policy.</p>"""
    accuracy_score: "aws_sdk_bedrock.types.automated_reasoning_policy_accuracy_score.AutomatedReasoningPolicyAccuracyScore"
    """<p>A score from 0.0 to 1.0 indicating how accurate the policy rules are relative to the source documents. A higher score means the policy rules more faithfully represent the source material.</p>"""
    rule_reports: "aws_sdk_bedrock.types.automated_reasoning_policy_rule_report_map.AutomatedReasoningPolicyRuleReportMap"
    """<p>A mapping from rule identifiers to detailed fidelity reports for each rule, showing which source statements ground each rule and how accurate it is.</p>"""
    variable_reports: "aws_sdk_bedrock.types.automated_reasoning_policy_variable_report_map.AutomatedReasoningPolicyVariableReportMap"
    """<p>A mapping from variable names to detailed fidelity reports for each variable, showing which source statements ground each variable and how accurate it is.</p>"""
    document_sources: "aws_sdk_bedrock.types.automated_reasoning_policy_report_source_document_list.AutomatedReasoningPolicyReportSourceDocumentList"
    """<p>A list of source documents with their content broken down into atomic statements and annotated with line numbers for precise referencing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyFidelityReport) -> dict:
    out: dict = {}
    out["coverageScore"] = value["coverage_score"]
    out["accuracyScore"] = value["accuracy_score"]
    import aws_sdk_bedrock.types.automated_reasoning_policy_rule_report_map

    out["ruleReports"] = (
        aws_sdk_bedrock.types.automated_reasoning_policy_rule_report_map.serialize_json(
            value["rule_reports"]
        )
    )
    import aws_sdk_bedrock.types.automated_reasoning_policy_variable_report_map

    out["variableReports"] = (
        aws_sdk_bedrock.types.automated_reasoning_policy_variable_report_map.serialize_json(
            value["variable_reports"]
        )
    )
    import aws_sdk_bedrock.types.automated_reasoning_policy_report_source_document_list

    out["documentSources"] = (
        aws_sdk_bedrock.types.automated_reasoning_policy_report_source_document_list.serialize_json(
            value["document_sources"]
        )
    )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyFidelityReport:
    out: AutomatedReasoningPolicyFidelityReport = {}  # type: ignore[typeddict-item]
    if "coverageScore" in data:
        out["coverage_score"] = data["coverageScore"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyFidelityReport.coverage_score required"
        )
    if "accuracyScore" in data:
        out["accuracy_score"] = data["accuracyScore"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyFidelityReport.accuracy_score required"
        )
    if "ruleReports" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_rule_report_map

        out["rule_reports"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_rule_report_map.deserialize_json(
                data["ruleReports"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyFidelityReport.rule_reports required"
        )
    if "variableReports" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_variable_report_map

        out["variable_reports"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_variable_report_map.deserialize_json(
                data["variableReports"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyFidelityReport.variable_reports required"
        )
    if "documentSources" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_report_source_document_list

        out["document_sources"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_report_source_document_list.deserialize_json(
                data["documentSources"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyFidelityReport.document_sources required"
        )
    return out
