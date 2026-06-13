"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedJobParameters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.analysis_template_arn
    import aws_sdk_cleanrooms.types.job_parameter_map


class ProtectedJobParameters(TypedDict):
    analysis_template_arn: (
        "aws_sdk_cleanrooms.types.analysis_template_arn.AnalysisTemplateArn"
    )
    """<p> The ARN of the analysis template.</p>"""
    parameters: NotRequired[
        "aws_sdk_cleanrooms.types.job_parameter_map.JobParameterMap"
    ]
    """<p>Runtime configuration values passed to the PySpark analysis script. Parameter names and types must match those defined in the analysis template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedJobParameters) -> dict:
    out: dict = {}
    out["analysisTemplateArn"] = value["analysis_template_arn"]
    if "parameters" in value:
        import aws_sdk_cleanrooms.types.job_parameter_map

        out["parameters"] = aws_sdk_cleanrooms.types.job_parameter_map.serialize_json(
            value["parameters"]
        )
    return out


def deserialize_json(data: dict) -> ProtectedJobParameters:
    out: ProtectedJobParameters = {}  # type: ignore[typeddict-item]
    if "analysisTemplateArn" in data:
        out["analysis_template_arn"] = data["analysisTemplateArn"]
    else:
        raise DeserializationError(
            "ProtectedJobParameters.analysis_template_arn required"
        )
    if "parameters" in data:
        import aws_sdk_cleanrooms.types.job_parameter_map

        out["parameters"] = aws_sdk_cleanrooms.types.job_parameter_map.deserialize_json(
            data["parameters"]
        )
    return out
