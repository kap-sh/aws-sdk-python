"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#ApplicationDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis_analytics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics.types.application_code
    import aws_sdk_kinesis_analytics.types.application_description
    import aws_sdk_kinesis_analytics.types.application_name
    import aws_sdk_kinesis_analytics.types.application_status
    import aws_sdk_kinesis_analytics.types.application_version_id
    import aws_sdk_kinesis_analytics.types.cloud_watch_logging_option_descriptions
    import aws_sdk_kinesis_analytics.types.input_descriptions
    import aws_sdk_kinesis_analytics.types.output_descriptions
    import aws_sdk_kinesis_analytics.types.reference_data_source_descriptions
    import aws_sdk_kinesis_analytics.types.resource_arn
    import aws_sdk_kinesis_analytics.types.timestamp


class ApplicationDetail(TypedDict):
    application_name: "aws_sdk_kinesis_analytics.types.application_name.ApplicationName"
    """<p>Name of the application.</p>"""
    application_description: NotRequired[
        "aws_sdk_kinesis_analytics.types.application_description.ApplicationDescription"
    ]
    """<p>Description of the application.</p>"""
    application_arn: "aws_sdk_kinesis_analytics.types.resource_arn.ResourceARN"
    """<p>ARN of the application.</p>"""
    application_status: (
        "aws_sdk_kinesis_analytics.types.application_status.ApplicationStatus"
    )
    """<p>Status of the application.</p>"""
    create_timestamp: NotRequired["aws_sdk_kinesis_analytics.types.timestamp.Timestamp"]
    """<p>Time stamp when the application version was created.</p>"""
    last_update_timestamp: NotRequired[
        "aws_sdk_kinesis_analytics.types.timestamp.Timestamp"
    ]
    """<p>Time stamp when the application was last updated.</p>"""
    input_descriptions: NotRequired[
        "aws_sdk_kinesis_analytics.types.input_descriptions.InputDescriptions"
    ]
    """<p>Describes the application input configuration. For more information, see <a href=\"https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-input.html\">Configuring Application Input</a>. </p>"""
    output_descriptions: NotRequired[
        "aws_sdk_kinesis_analytics.types.output_descriptions.OutputDescriptions"
    ]
    """<p>Describes the application output configuration. For more information, see <a href=\"https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-output.html\">Configuring Application Output</a>. </p>"""
    reference_data_source_descriptions: NotRequired[
        "aws_sdk_kinesis_analytics.types.reference_data_source_descriptions.ReferenceDataSourceDescriptions"
    ]
    """<p>Describes reference data sources configured for the application. For more information, see <a href=\"https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-input.html\">Configuring Application Input</a>. </p>"""
    cloud_watch_logging_option_descriptions: NotRequired[
        "aws_sdk_kinesis_analytics.types.cloud_watch_logging_option_descriptions.CloudWatchLoggingOptionDescriptions"
    ]
    """<p>Describes the CloudWatch log streams that are configured to receive application messages. For more information about using CloudWatch log streams with Amazon Kinesis Analytics applications, see <a href=\"https://docs.aws.amazon.com/kinesisanalytics/latest/dev/cloudwatch-logs.html\">Working with Amazon CloudWatch Logs</a>. </p>"""
    application_code: NotRequired[
        "aws_sdk_kinesis_analytics.types.application_code.ApplicationCode"
    ]
    """<p>Returns the application code that you provided to perform data analysis on any of the in-application streams in your application.</p>"""
    application_version_id: (
        "aws_sdk_kinesis_analytics.types.application_version_id.ApplicationVersionId"
    )
    """<p>Provides the current application version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationDetail) -> dict:
    out: dict = {}
    out["ApplicationName"] = value["application_name"]
    if "application_description" in value:
        out["ApplicationDescription"] = value["application_description"]
    out["ApplicationARN"] = value["application_arn"]
    import aws_sdk_kinesis_analytics.types.application_status

    out["ApplicationStatus"] = (
        aws_sdk_kinesis_analytics.types.application_status.serialize_aws_json_1_1(
            value["application_status"]
        )
    )
    if "create_timestamp" in value:
        import aws_sdk_kinesis_analytics.types.timestamp

        out["CreateTimestamp"] = (
            aws_sdk_kinesis_analytics.types.timestamp.serialize_aws_json_1_1(
                value["create_timestamp"]
            )
        )
    if "last_update_timestamp" in value:
        import aws_sdk_kinesis_analytics.types.timestamp

        out["LastUpdateTimestamp"] = (
            aws_sdk_kinesis_analytics.types.timestamp.serialize_aws_json_1_1(
                value["last_update_timestamp"]
            )
        )
    if "input_descriptions" in value:
        import aws_sdk_kinesis_analytics.types.input_descriptions

        out["InputDescriptions"] = (
            aws_sdk_kinesis_analytics.types.input_descriptions.serialize_aws_json_1_1(
                value["input_descriptions"]
            )
        )
    if "output_descriptions" in value:
        import aws_sdk_kinesis_analytics.types.output_descriptions

        out["OutputDescriptions"] = (
            aws_sdk_kinesis_analytics.types.output_descriptions.serialize_aws_json_1_1(
                value["output_descriptions"]
            )
        )
    if "reference_data_source_descriptions" in value:
        import aws_sdk_kinesis_analytics.types.reference_data_source_descriptions

        out["ReferenceDataSourceDescriptions"] = (
            aws_sdk_kinesis_analytics.types.reference_data_source_descriptions.serialize_aws_json_1_1(
                value["reference_data_source_descriptions"]
            )
        )
    if "cloud_watch_logging_option_descriptions" in value:
        import aws_sdk_kinesis_analytics.types.cloud_watch_logging_option_descriptions

        out["CloudWatchLoggingOptionDescriptions"] = (
            aws_sdk_kinesis_analytics.types.cloud_watch_logging_option_descriptions.serialize_aws_json_1_1(
                value["cloud_watch_logging_option_descriptions"]
            )
        )
    if "application_code" in value:
        out["ApplicationCode"] = value["application_code"]
    out["ApplicationVersionId"] = value["application_version_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationDetail:
    out: ApplicationDetail = {}  # type: ignore[typeddict-item]
    if "ApplicationName" in data:
        out["application_name"] = data["ApplicationName"]
    else:
        raise DeserializationError("ApplicationDetail.application_name required")
    if "ApplicationDescription" in data:
        out["application_description"] = data["ApplicationDescription"]
    if "ApplicationARN" in data:
        out["application_arn"] = data["ApplicationARN"]
    else:
        raise DeserializationError("ApplicationDetail.application_arn required")
    if "ApplicationStatus" in data:
        import aws_sdk_kinesis_analytics.types.application_status

        out["application_status"] = (
            aws_sdk_kinesis_analytics.types.application_status.deserialize_aws_json_1_1(
                data["ApplicationStatus"]
            )
        )
    else:
        raise DeserializationError("ApplicationDetail.application_status required")
    if "CreateTimestamp" in data:
        import aws_sdk_kinesis_analytics.types.timestamp

        out["create_timestamp"] = (
            aws_sdk_kinesis_analytics.types.timestamp.deserialize_aws_json_1_1(
                data["CreateTimestamp"]
            )
        )
    if "LastUpdateTimestamp" in data:
        import aws_sdk_kinesis_analytics.types.timestamp

        out["last_update_timestamp"] = (
            aws_sdk_kinesis_analytics.types.timestamp.deserialize_aws_json_1_1(
                data["LastUpdateTimestamp"]
            )
        )
    if "InputDescriptions" in data:
        import aws_sdk_kinesis_analytics.types.input_descriptions

        out["input_descriptions"] = (
            aws_sdk_kinesis_analytics.types.input_descriptions.deserialize_aws_json_1_1(
                data["InputDescriptions"]
            )
        )
    if "OutputDescriptions" in data:
        import aws_sdk_kinesis_analytics.types.output_descriptions

        out["output_descriptions"] = (
            aws_sdk_kinesis_analytics.types.output_descriptions.deserialize_aws_json_1_1(
                data["OutputDescriptions"]
            )
        )
    if "ReferenceDataSourceDescriptions" in data:
        import aws_sdk_kinesis_analytics.types.reference_data_source_descriptions

        out["reference_data_source_descriptions"] = (
            aws_sdk_kinesis_analytics.types.reference_data_source_descriptions.deserialize_aws_json_1_1(
                data["ReferenceDataSourceDescriptions"]
            )
        )
    if "CloudWatchLoggingOptionDescriptions" in data:
        import aws_sdk_kinesis_analytics.types.cloud_watch_logging_option_descriptions

        out["cloud_watch_logging_option_descriptions"] = (
            aws_sdk_kinesis_analytics.types.cloud_watch_logging_option_descriptions.deserialize_aws_json_1_1(
                data["CloudWatchLoggingOptionDescriptions"]
            )
        )
    if "ApplicationCode" in data:
        out["application_code"] = data["ApplicationCode"]
    if "ApplicationVersionId" in data:
        out["application_version_id"] = data["ApplicationVersionId"]
    else:
        raise DeserializationError("ApplicationDetail.application_version_id required")
    return out
