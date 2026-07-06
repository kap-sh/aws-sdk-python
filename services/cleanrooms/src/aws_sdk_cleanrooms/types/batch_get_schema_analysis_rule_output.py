"""Generated from Smithy shape ``com.amazonaws.cleanrooms#BatchGetSchemaAnalysisRuleOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.batch_get_schema_analysis_rule_error_list
    import aws_sdk_cleanrooms.types.schema_analysis_rule_list


class BatchGetSchemaAnalysisRuleOutput(TypedDict, closed=True):
    analysis_rules: (
        "aws_sdk_cleanrooms.types.schema_analysis_rule_list.SchemaAnalysisRuleList"
    )
    """<p>The retrieved list of analysis rules.</p>"""
    errors: "aws_sdk_cleanrooms.types.batch_get_schema_analysis_rule_error_list.BatchGetSchemaAnalysisRuleErrorList"
    """<p>Error reasons for schemas that could not be retrieved. One error is returned for every schema that could not be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetSchemaAnalysisRuleOutput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.schema_analysis_rule_list

    out["analysisRules"] = (
        aws_sdk_cleanrooms.types.schema_analysis_rule_list.serialize_json(
            value["analysis_rules"]
        )
    )
    import aws_sdk_cleanrooms.types.batch_get_schema_analysis_rule_error_list

    out["errors"] = (
        aws_sdk_cleanrooms.types.batch_get_schema_analysis_rule_error_list.serialize_json(
            value["errors"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetSchemaAnalysisRuleOutput:
    out: BatchGetSchemaAnalysisRuleOutput = {}  # type: ignore[typeddict-item]
    if "analysisRules" in data:
        import aws_sdk_cleanrooms.types.schema_analysis_rule_list

        out["analysis_rules"] = (
            aws_sdk_cleanrooms.types.schema_analysis_rule_list.deserialize_json(
                data["analysisRules"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetSchemaAnalysisRuleOutput.analysis_rules required"
        )
    if "errors" in data:
        import aws_sdk_cleanrooms.types.batch_get_schema_analysis_rule_error_list

        out["errors"] = (
            aws_sdk_cleanrooms.types.batch_get_schema_analysis_rule_error_list.deserialize_json(
                data["errors"]
            )
        )
    else:
        raise DeserializationError("BatchGetSchemaAnalysisRuleOutput.errors required")
    return out
