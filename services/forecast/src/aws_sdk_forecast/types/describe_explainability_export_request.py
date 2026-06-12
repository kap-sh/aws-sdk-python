"""Generated from Smithy shape ``com.amazonaws.forecast#DescribeExplainabilityExportRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_forecast.types.arn


class DescribeExplainabilityExportRequest(TypedDict):
    explainability_export_arn: "aws_sdk_forecast.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the Explainability export.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeExplainabilityExportRequest) -> dict:
    out: dict = {}
    out["ExplainabilityExportArn"] = value["explainability_export_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeExplainabilityExportRequest:
    out: DescribeExplainabilityExportRequest = {}  # type: ignore[typeddict-item]
    if "ExplainabilityExportArn" in data:
        out["explainability_export_arn"] = data["ExplainabilityExportArn"]
    else:
        raise DeserializationError(
            "DescribeExplainabilityExportRequest.explainability_export_arn required"
        )
    return out
