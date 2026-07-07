"""Generated from Smithy shape ``com.amazonaws.forecast#CreateExplainabilityExportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_forecast.types.arn


class CreateExplainabilityExportResponse(TypedDict, closed=True):
    explainability_export_arn: NotRequired["aws_sdk_forecast.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the export.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateExplainabilityExportResponse) -> dict:
    out: dict = {}
    if "explainability_export_arn" in value:
        out["ExplainabilityExportArn"] = value["explainability_export_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateExplainabilityExportResponse:
    out: CreateExplainabilityExportResponse = {}  # type: ignore[typeddict-item]
    if "ExplainabilityExportArn" in data:
        out["explainability_export_arn"] = data["ExplainabilityExportArn"]
    return out
