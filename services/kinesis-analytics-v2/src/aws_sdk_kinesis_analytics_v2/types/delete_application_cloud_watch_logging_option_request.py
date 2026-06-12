"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#DeleteApplicationCloudWatchLoggingOptionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.application_name
    import aws_sdk_kinesis_analytics_v2.types.application_version_id
    import aws_sdk_kinesis_analytics_v2.types.conditional_token
    import aws_sdk_kinesis_analytics_v2.types.id


class DeleteApplicationCloudWatchLoggingOptionRequest(TypedDict):
    application_name: (
        "aws_sdk_kinesis_analytics_v2.types.application_name.ApplicationName"
    )
    """<p>The application name.</p>"""
    current_application_version_id: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.application_version_id.ApplicationVersionId"
    ]
    """<p>The version ID of the application. You must provide the <code>CurrentApplicationVersionId</code> or the <code>ConditionalToken</code>. You can retrieve the application version ID using <a>DescribeApplication</a>. For better concurrency support, use the <code>ConditionalToken</code> parameter instead of <code>CurrentApplicationVersionId</code>.</p>"""
    cloud_watch_logging_option_id: "aws_sdk_kinesis_analytics_v2.types.id.Id"
    """<p>The <code>CloudWatchLoggingOptionId</code> of the Amazon CloudWatch logging option to delete. You can get the <code>CloudWatchLoggingOptionId</code> by using the <a>DescribeApplication</a> operation. </p>"""
    conditional_token: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.conditional_token.ConditionalToken"
    ]
    """<p>A value you use to implement strong concurrency for application updates. You must provide the <code>CurrentApplicationVersionId</code> or the <code>ConditionalToken</code>. You get the application's current <code>ConditionalToken</code> using <a>DescribeApplication</a>. For better concurrency support, use the <code>ConditionalToken</code> parameter instead of <code>CurrentApplicationVersionId</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DeleteApplicationCloudWatchLoggingOptionRequest,
) -> dict:
    out: dict = {}
    out["ApplicationName"] = value["application_name"]
    if "current_application_version_id" in value:
        out["CurrentApplicationVersionId"] = value["current_application_version_id"]
    out["CloudWatchLoggingOptionId"] = value["cloud_watch_logging_option_id"]
    if "conditional_token" in value:
        out["ConditionalToken"] = value["conditional_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DeleteApplicationCloudWatchLoggingOptionRequest:
    out: DeleteApplicationCloudWatchLoggingOptionRequest = {}  # type: ignore[typeddict-item]
    if "ApplicationName" in data:
        out["application_name"] = data["ApplicationName"]
    else:
        raise DeserializationError(
            "DeleteApplicationCloudWatchLoggingOptionRequest.application_name required"
        )
    if "CurrentApplicationVersionId" in data:
        out["current_application_version_id"] = data["CurrentApplicationVersionId"]
    if "CloudWatchLoggingOptionId" in data:
        out["cloud_watch_logging_option_id"] = data["CloudWatchLoggingOptionId"]
    else:
        raise DeserializationError(
            "DeleteApplicationCloudWatchLoggingOptionRequest.cloud_watch_logging_option_id required"
        )
    if "ConditionalToken" in data:
        out["conditional_token"] = data["ConditionalToken"]
    return out
