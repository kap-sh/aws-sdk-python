"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#DeleteApplicationCloudWatchLoggingOptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_kinesis_analytics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics.types.application_name
    import aws_sdk_kinesis_analytics.types.application_version_id
    import aws_sdk_kinesis_analytics.types.id


class DeleteApplicationCloudWatchLoggingOptionRequest(TypedDict, closed=True):
    application_name: "aws_sdk_kinesis_analytics.types.application_name.ApplicationName"
    """<p>The Kinesis Analytics application name.</p>"""
    current_application_version_id: (
        "aws_sdk_kinesis_analytics.types.application_version_id.ApplicationVersionId"
    )
    """<p>The version ID of the Kinesis Analytics application.</p>"""
    cloud_watch_logging_option_id: "aws_sdk_kinesis_analytics.types.id.Id"
    r"""<p>The <code>CloudWatchLoggingOptionId</code> of the CloudWatch logging option to delete. You can get the <code>CloudWatchLoggingOptionId</code> by using the <a href=\"https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html\">DescribeApplication</a> operation. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DeleteApplicationCloudWatchLoggingOptionRequest,
) -> dict:
    out: dict = {}
    out["ApplicationName"] = value["application_name"]
    out["CurrentApplicationVersionId"] = value["current_application_version_id"]
    out["CloudWatchLoggingOptionId"] = value["cloud_watch_logging_option_id"]
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
    else:
        raise DeserializationError(
            "DeleteApplicationCloudWatchLoggingOptionRequest.current_application_version_id required"
        )
    if "CloudWatchLoggingOptionId" in data:
        out["cloud_watch_logging_option_id"] = data["CloudWatchLoggingOptionId"]
    else:
        raise DeserializationError(
            "DeleteApplicationCloudWatchLoggingOptionRequest.cloud_watch_logging_option_id required"
        )
    return out
