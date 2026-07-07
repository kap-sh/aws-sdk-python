"""Generated from Smithy shape ``com.amazonaws.cleanrooms#SchemaStatusDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.analysis_rule_type
    import aws_sdk_cleanrooms.types.analysis_type
    import aws_sdk_cleanrooms.types.schema_configuration_list
    import aws_sdk_cleanrooms.types.schema_status
    import aws_sdk_cleanrooms.types.schema_status_reason_list


class SchemaStatusDetail(TypedDict, closed=True):
    status: "aws_sdk_cleanrooms.types.schema_status.SchemaStatus"
    """<p>The status of the schema, indicating if it is ready to query.</p>"""
    reasons: NotRequired[
        "aws_sdk_cleanrooms.types.schema_status_reason_list.SchemaStatusReasonList"
    ]
    """<p>The reasons why the schema status is set to its current state.</p>"""
    analysis_rule_type: NotRequired[
        "aws_sdk_cleanrooms.types.analysis_rule_type.AnalysisRuleType"
    ]
    """<p>The analysis rule type for which the schema status has been evaluated.</p>"""
    configurations: NotRequired[
        "aws_sdk_cleanrooms.types.schema_configuration_list.SchemaConfigurationList"
    ]
    """<p>The configuration details of the schema analysis rule for the given type.</p>"""
    analysis_type: "aws_sdk_cleanrooms.types.analysis_type.AnalysisType"
    """<p>The type of analysis that can be performed on the schema.</p> <p>A schema can have an <code>analysisType</code> of <code>DIRECT_ANALYSIS</code>, <code>ADDITIONAL_ANALYSIS_FOR_AUDIENCE_GENERATION</code>, or both.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SchemaStatusDetail) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.schema_status

    out["status"] = aws_sdk_cleanrooms.types.schema_status.serialize_json(
        value["status"]
    )
    if "reasons" in value:
        import aws_sdk_cleanrooms.types.schema_status_reason_list

        out["reasons"] = (
            aws_sdk_cleanrooms.types.schema_status_reason_list.serialize_json(
                value["reasons"]
            )
        )
    if "analysis_rule_type" in value:
        import aws_sdk_cleanrooms.types.analysis_rule_type

        out["analysisRuleType"] = (
            aws_sdk_cleanrooms.types.analysis_rule_type.serialize_json(
                value["analysis_rule_type"]
            )
        )
    if "configurations" in value:
        import aws_sdk_cleanrooms.types.schema_configuration_list

        out["configurations"] = (
            aws_sdk_cleanrooms.types.schema_configuration_list.serialize_json(
                value["configurations"]
            )
        )
    import aws_sdk_cleanrooms.types.analysis_type

    out["analysisType"] = aws_sdk_cleanrooms.types.analysis_type.serialize_json(
        value["analysis_type"]
    )
    return out


def deserialize_json(data: dict) -> SchemaStatusDetail:
    out: SchemaStatusDetail = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_cleanrooms.types.schema_status

        out["status"] = aws_sdk_cleanrooms.types.schema_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("SchemaStatusDetail.status required")
    if "reasons" in data:
        import aws_sdk_cleanrooms.types.schema_status_reason_list

        out["reasons"] = (
            aws_sdk_cleanrooms.types.schema_status_reason_list.deserialize_json(
                data["reasons"]
            )
        )
    if "analysisRuleType" in data:
        import aws_sdk_cleanrooms.types.analysis_rule_type

        out["analysis_rule_type"] = (
            aws_sdk_cleanrooms.types.analysis_rule_type.deserialize_json(
                data["analysisRuleType"]
            )
        )
    if "configurations" in data:
        import aws_sdk_cleanrooms.types.schema_configuration_list

        out["configurations"] = (
            aws_sdk_cleanrooms.types.schema_configuration_list.deserialize_json(
                data["configurations"]
            )
        )
    if "analysisType" in data:
        import aws_sdk_cleanrooms.types.analysis_type

        out["analysis_type"] = aws_sdk_cleanrooms.types.analysis_type.deserialize_json(
            data["analysisType"]
        )
    else:
        raise DeserializationError("SchemaStatusDetail.analysis_type required")
    return out
