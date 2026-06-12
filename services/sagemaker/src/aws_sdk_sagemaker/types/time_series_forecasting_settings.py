"""Generated from Smithy shape ``com.amazonaws.sagemaker#TimeSeriesForecastingSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.feature_status
    import aws_sdk_sagemaker.types.role_arn


class TimeSeriesForecastingSettings(TypedDict):
    status: NotRequired["aws_sdk_sagemaker.types.feature_status.FeatureStatus"]
    """<p>Describes whether time series forecasting is enabled or disabled in the Canvas application.</p>"""
    amazon_forecast_role_arn: NotRequired["aws_sdk_sagemaker.types.role_arn.RoleArn"]
    """<p>The IAM role that Canvas passes to Amazon Forecast for time series forecasting. By default, Canvas uses the execution role specified in the <code>UserProfile</code> that launches the Canvas application. If an execution role is not specified in the <code>UserProfile</code>, Canvas uses the execution role specified in the Domain that owns the <code>UserProfile</code>. To allow time series forecasting, this IAM role should have the <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/security-iam-awsmanpol-canvas.html#security-iam-awsmanpol-AmazonSageMakerCanvasForecastAccess\"> AmazonSageMakerCanvasForecastAccess</a> policy attached and <code>forecast.amazonaws.com</code> added in the trust relationship as a service principal.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TimeSeriesForecastingSettings) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_sagemaker.types.feature_status

        out["Status"] = aws_sdk_sagemaker.types.feature_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "amazon_forecast_role_arn" in value:
        out["AmazonForecastRoleArn"] = value["amazon_forecast_role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TimeSeriesForecastingSettings:
    out: TimeSeriesForecastingSettings = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_sagemaker.types.feature_status

        out["status"] = aws_sdk_sagemaker.types.feature_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "AmazonForecastRoleArn" in data:
        out["amazon_forecast_role_arn"] = data["AmazonForecastRoleArn"]
    return out
