"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#AddApplicationCloudWatchLoggingOptionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kinesis_analytics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics.types.application_name
    import aws_sdk_kinesis_analytics.types.application_version_id
    import aws_sdk_kinesis_analytics.types.cloud_watch_logging_option


class AddApplicationCloudWatchLoggingOptionRequest(TypedDict):
    application_name: "aws_sdk_kinesis_analytics.types.application_name.ApplicationName"
    """<p>The Kinesis Analytics application name.</p>"""
    current_application_version_id: (
        "aws_sdk_kinesis_analytics.types.application_version_id.ApplicationVersionId"
    )
    """<p>The version ID of the Kinesis Analytics application.</p>"""
    cloud_watch_logging_option: "aws_sdk_kinesis_analytics.types.cloud_watch_logging_option.CloudWatchLoggingOption"
    """<p>Provides the CloudWatch log stream Amazon Resource Name (ARN) and the IAM role ARN. Note: To write application messages to CloudWatch, the IAM role that is used must have the <code>PutLogEvents</code> policy action enabled.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddApplicationCloudWatchLoggingOptionRequest) -> dict:
    out: dict = {}
    out["ApplicationName"] = value["application_name"]
    out["CurrentApplicationVersionId"] = value["current_application_version_id"]
    import aws_sdk_kinesis_analytics.types.cloud_watch_logging_option

    out["CloudWatchLoggingOption"] = (
        aws_sdk_kinesis_analytics.types.cloud_watch_logging_option.serialize_aws_json_1_1(
            value["cloud_watch_logging_option"]
        )
    )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> AddApplicationCloudWatchLoggingOptionRequest:
    out: AddApplicationCloudWatchLoggingOptionRequest = {}  # type: ignore[typeddict-item]
    if "ApplicationName" in data:
        out["application_name"] = data["ApplicationName"]
    else:
        raise DeserializationError(
            "AddApplicationCloudWatchLoggingOptionRequest.application_name required"
        )
    if "CurrentApplicationVersionId" in data:
        out["current_application_version_id"] = data["CurrentApplicationVersionId"]
    else:
        raise DeserializationError(
            "AddApplicationCloudWatchLoggingOptionRequest.current_application_version_id required"
        )
    if "CloudWatchLoggingOption" in data:
        import aws_sdk_kinesis_analytics.types.cloud_watch_logging_option

        out["cloud_watch_logging_option"] = (
            aws_sdk_kinesis_analytics.types.cloud_watch_logging_option.deserialize_aws_json_1_1(
                data["CloudWatchLoggingOption"]
            )
        )
    else:
        raise DeserializationError(
            "AddApplicationCloudWatchLoggingOptionRequest.cloud_watch_logging_option required"
        )
    return out
