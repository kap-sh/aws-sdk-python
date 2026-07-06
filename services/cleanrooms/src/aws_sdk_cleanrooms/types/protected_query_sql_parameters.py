"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedQuerySQLParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.analysis_template_arn
    import aws_sdk_cleanrooms.types.parameter_map


class ProtectedQuerySQLParameters(TypedDict, closed=True):
    query_string: NotRequired["str"]
    """<p>The query string to be submitted.</p>"""
    analysis_template_arn: NotRequired[
        "aws_sdk_cleanrooms.types.analysis_template_arn.AnalysisTemplateArn"
    ]
    """<p>The Amazon Resource Name (ARN) associated with the analysis template within a collaboration.</p>"""
    parameters: NotRequired["aws_sdk_cleanrooms.types.parameter_map.ParameterMap"]
    """<p>The protected query SQL parameters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedQuerySQLParameters) -> dict:
    out: dict = {}
    if "query_string" in value:
        out["queryString"] = value["query_string"]
    if "analysis_template_arn" in value:
        out["analysisTemplateArn"] = value["analysis_template_arn"]
    if "parameters" in value:
        import aws_sdk_cleanrooms.types.parameter_map

        out["parameters"] = aws_sdk_cleanrooms.types.parameter_map.serialize_json(
            value["parameters"]
        )
    return out


def deserialize_json(data: dict) -> ProtectedQuerySQLParameters:
    out: ProtectedQuerySQLParameters = {}  # type: ignore[typeddict-item]
    if "queryString" in data:
        out["query_string"] = data["queryString"]
    if "analysisTemplateArn" in data:
        out["analysis_template_arn"] = data["analysisTemplateArn"]
    if "parameters" in data:
        import aws_sdk_cleanrooms.types.parameter_map

        out["parameters"] = aws_sdk_cleanrooms.types.parameter_map.deserialize_json(
            data["parameters"]
        )
    return out
