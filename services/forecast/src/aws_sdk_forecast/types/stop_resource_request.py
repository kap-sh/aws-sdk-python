"""Generated from Smithy shape ``com.amazonaws.forecast#StopResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_forecast.types.arn


class StopResourceRequest(TypedDict):
    resource_arn: "aws_sdk_forecast.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that identifies the resource to stop. The supported ARNs are <code>DatasetImportJobArn</code>, <code>PredictorArn</code>, <code>PredictorBacktestExportJobArn</code>, <code>ForecastArn</code>, <code>ForecastExportJobArn</code>, <code>ExplainabilityArn</code>, and <code>ExplainabilityExportArn</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopResourceRequest:
    out: StopResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("StopResourceRequest.resource_arn required")
    return out
