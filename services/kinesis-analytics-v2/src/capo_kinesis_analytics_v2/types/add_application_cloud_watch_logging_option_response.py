"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#AddApplicationCloudWatchLoggingOptionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.application_version_id
    import capo_kinesis_analytics_v2.types.cloud_watch_logging_option_descriptions
    import capo_kinesis_analytics_v2.types.operation_id
    import capo_kinesis_analytics_v2.types.resource_arn


class AddApplicationCloudWatchLoggingOptionResponse(TypedDict, closed=True):
    application_arn: NotRequired[
        "capo_kinesis_analytics_v2.types.resource_arn.ResourceARN"
    ]
    """<p>The application's ARN.</p>"""
    application_version_id: NotRequired[
        "capo_kinesis_analytics_v2.types.application_version_id.ApplicationVersionId"
    ]
    """<p>The new version ID of the SQL-based Kinesis Data Analytics application. Kinesis Data Analytics updates the <code>ApplicationVersionId</code> each time you change the CloudWatch logging options. </p>"""
    cloud_watch_logging_option_descriptions: NotRequired[
        "capo_kinesis_analytics_v2.types.cloud_watch_logging_option_descriptions.CloudWatchLoggingOptionDescriptions"
    ]
    """<p>The descriptions of the current CloudWatch logging options for the SQL-based Kinesis Data Analytics application.</p>"""
    operation_id: NotRequired[
        "capo_kinesis_analytics_v2.types.operation_id.OperationId"
    ]
    """<p>The operation ID that can be used to track the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: AddApplicationCloudWatchLoggingOptionResponse,
) -> dict:
    out: dict = {}
    if "application_arn" in value:
        out["ApplicationARN"] = value["application_arn"]
    if "application_version_id" in value:
        out["ApplicationVersionId"] = value["application_version_id"]
    if "cloud_watch_logging_option_descriptions" in value:
        import capo_kinesis_analytics_v2.types.cloud_watch_logging_option_descriptions

        out["CloudWatchLoggingOptionDescriptions"] = (
            capo_kinesis_analytics_v2.types.cloud_watch_logging_option_descriptions.serialize_aws_json_1_1(
                value["cloud_watch_logging_option_descriptions"]
            )
        )
    if "operation_id" in value:
        out["OperationId"] = value["operation_id"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> AddApplicationCloudWatchLoggingOptionResponse:
    out: AddApplicationCloudWatchLoggingOptionResponse = {}  # type: ignore[typeddict-item]
    if "ApplicationARN" in data:
        out["application_arn"] = data["ApplicationARN"]
    if "ApplicationVersionId" in data:
        out["application_version_id"] = data["ApplicationVersionId"]
    if "CloudWatchLoggingOptionDescriptions" in data:
        import capo_kinesis_analytics_v2.types.cloud_watch_logging_option_descriptions

        out["cloud_watch_logging_option_descriptions"] = (
            capo_kinesis_analytics_v2.types.cloud_watch_logging_option_descriptions.deserialize_aws_json_1_1(
                data["CloudWatchLoggingOptionDescriptions"]
            )
        )
    if "OperationId" in data:
        out["operation_id"] = data["OperationId"]
    return out
