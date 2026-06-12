"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#DeleteApplicationCloudWatchLoggingOptionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.application_version_id
    import aws_sdk_kinesis_analytics_v2.types.cloud_watch_logging_option_descriptions
    import aws_sdk_kinesis_analytics_v2.types.operation_id
    import aws_sdk_kinesis_analytics_v2.types.resource_arn


class DeleteApplicationCloudWatchLoggingOptionResponse(TypedDict):
    application_arn: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.resource_arn.ResourceARN"
    ]
    """<p>The application's Amazon Resource Name (ARN).</p>"""
    application_version_id: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.application_version_id.ApplicationVersionId"
    ]
    """<p>The version ID of the application. Kinesis Data Analytics updates the <code>ApplicationVersionId</code> each time you change the CloudWatch logging options.</p>"""
    cloud_watch_logging_option_descriptions: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.cloud_watch_logging_option_descriptions.CloudWatchLoggingOptionDescriptions"
    ]
    """<p>The descriptions of the remaining CloudWatch logging options for the application.</p>"""
    operation_id: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.operation_id.OperationId"
    ]
    """<p>The operation ID that can be used to track the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DeleteApplicationCloudWatchLoggingOptionResponse,
) -> dict:
    out: dict = {}
    if "application_arn" in value:
        out["ApplicationARN"] = value["application_arn"]
    if "application_version_id" in value:
        out["ApplicationVersionId"] = value["application_version_id"]
    if "cloud_watch_logging_option_descriptions" in value:
        import aws_sdk_kinesis_analytics_v2.types.cloud_watch_logging_option_descriptions

        out["CloudWatchLoggingOptionDescriptions"] = (
            aws_sdk_kinesis_analytics_v2.types.cloud_watch_logging_option_descriptions.serialize_aws_json_1_1(
                value["cloud_watch_logging_option_descriptions"]
            )
        )
    if "operation_id" in value:
        out["OperationId"] = value["operation_id"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DeleteApplicationCloudWatchLoggingOptionResponse:
    out: DeleteApplicationCloudWatchLoggingOptionResponse = {}  # type: ignore[typeddict-item]
    if "ApplicationARN" in data:
        out["application_arn"] = data["ApplicationARN"]
    if "ApplicationVersionId" in data:
        out["application_version_id"] = data["ApplicationVersionId"]
    if "CloudWatchLoggingOptionDescriptions" in data:
        import aws_sdk_kinesis_analytics_v2.types.cloud_watch_logging_option_descriptions

        out["cloud_watch_logging_option_descriptions"] = (
            aws_sdk_kinesis_analytics_v2.types.cloud_watch_logging_option_descriptions.deserialize_aws_json_1_1(
                data["CloudWatchLoggingOptionDescriptions"]
            )
        )
    if "OperationId" in data:
        out["operation_id"] = data["OperationId"]
    return out
