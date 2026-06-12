"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#CreateApplicationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis_analytics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics.types.application_code
    import aws_sdk_kinesis_analytics.types.application_description
    import aws_sdk_kinesis_analytics.types.application_name
    import aws_sdk_kinesis_analytics.types.cloud_watch_logging_options
    import aws_sdk_kinesis_analytics.types.inputs
    import aws_sdk_kinesis_analytics.types.outputs
    import aws_sdk_kinesis_analytics.types.tags


class CreateApplicationRequest(TypedDict):
    application_name: "aws_sdk_kinesis_analytics.types.application_name.ApplicationName"
    """<p>Name of your Amazon Kinesis Analytics application (for example, <code>sample-app</code>).</p>"""
    application_description: NotRequired[
        "aws_sdk_kinesis_analytics.types.application_description.ApplicationDescription"
    ]
    """<p>Summary description of the application.</p>"""
    inputs: NotRequired["aws_sdk_kinesis_analytics.types.inputs.Inputs"]
    """<p>Use this parameter to configure the application input.</p> <p>You can configure your application to receive input from a single streaming source. In this configuration, you map this streaming source to an in-application stream that is created. Your application code can then query the in-application stream like a table (you can think of it as a constantly updating table).</p> <p>For the streaming source, you provide its Amazon Resource Name (ARN) and format of data on the stream (for example, JSON, CSV, etc.). You also must provide an IAM role that Amazon Kinesis Analytics can assume to read this stream on your behalf.</p> <p>To create the in-application stream, you need to specify a schema to transform your data into a schematized version used in SQL. In the schema, you provide the necessary mapping of the data elements in the streaming source to record columns in the in-app stream.</p>"""
    outputs: NotRequired["aws_sdk_kinesis_analytics.types.outputs.Outputs"]
    """<p>You can configure application output to write data from any of the in-application streams to up to three destinations.</p> <p>These destinations can be Amazon Kinesis streams, Amazon Kinesis Firehose delivery streams, AWS Lambda destinations, or any combination of the three.</p> <p>In the configuration, you specify the in-application stream name, the destination stream or Lambda function Amazon Resource Name (ARN), and the format to use when writing data. You must also provide an IAM role that Amazon Kinesis Analytics can assume to write to the destination stream or Lambda function on your behalf.</p> <p>In the output configuration, you also provide the output stream or Lambda function ARN. For stream destinations, you provide the format of data in the stream (for example, JSON, CSV). You also must provide an IAM role that Amazon Kinesis Analytics can assume to write to the stream or Lambda function on your behalf.</p>"""
    cloud_watch_logging_options: NotRequired[
        "aws_sdk_kinesis_analytics.types.cloud_watch_logging_options.CloudWatchLoggingOptions"
    ]
    """<p>Use this parameter to configure a CloudWatch log stream to monitor application configuration errors. For more information, see <a href=\"https://docs.aws.amazon.com/kinesisanalytics/latest/dev/cloudwatch-logs.html\">Working with Amazon CloudWatch Logs</a>.</p>"""
    application_code: NotRequired[
        "aws_sdk_kinesis_analytics.types.application_code.ApplicationCode"
    ]
    """<p>One or more SQL statements that read input data, transform it, and generate output. For example, you can write a SQL statement that reads data from one in-application stream, generates a running average of the number of advertisement clicks by vendor, and insert resulting rows in another in-application stream using pumps. For more information about the typical pattern, see <a href=\"https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-app-code.html\">Application Code</a>. </p> <p>You can provide such series of SQL statements, where output of one statement can be used as the input for the next statement. You store intermediate results by creating in-application streams and pumps.</p> <p>Note that the application code must create the streams with names specified in the <code>Outputs</code>. For example, if your <code>Outputs</code> defines output streams named <code>ExampleOutputStream1</code> and <code>ExampleOutputStream2</code>, then your application code must create these streams. </p>"""
    tags: NotRequired["aws_sdk_kinesis_analytics.types.tags.Tags"]
    """<p>A list of one or more tags to assign to the application. A tag is a key-value pair that identifies an application. Note that the maximum number of application tags includes system tags. The maximum number of user-defined application tags is 50. For more information, see <a href=\"https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-tagging.html\">Using Tagging</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateApplicationRequest) -> dict:
    out: dict = {}
    out["ApplicationName"] = value["application_name"]
    if "application_description" in value:
        out["ApplicationDescription"] = value["application_description"]
    if "inputs" in value:
        import aws_sdk_kinesis_analytics.types.inputs

        out["Inputs"] = aws_sdk_kinesis_analytics.types.inputs.serialize_aws_json_1_1(
            value["inputs"]
        )
    if "outputs" in value:
        import aws_sdk_kinesis_analytics.types.outputs

        out["Outputs"] = aws_sdk_kinesis_analytics.types.outputs.serialize_aws_json_1_1(
            value["outputs"]
        )
    if "cloud_watch_logging_options" in value:
        import aws_sdk_kinesis_analytics.types.cloud_watch_logging_options

        out["CloudWatchLoggingOptions"] = (
            aws_sdk_kinesis_analytics.types.cloud_watch_logging_options.serialize_aws_json_1_1(
                value["cloud_watch_logging_options"]
            )
        )
    if "application_code" in value:
        out["ApplicationCode"] = value["application_code"]
    if "tags" in value:
        import aws_sdk_kinesis_analytics.types.tags

        out["Tags"] = aws_sdk_kinesis_analytics.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateApplicationRequest:
    out: CreateApplicationRequest = {}  # type: ignore[typeddict-item]
    if "ApplicationName" in data:
        out["application_name"] = data["ApplicationName"]
    else:
        raise DeserializationError("CreateApplicationRequest.application_name required")
    if "ApplicationDescription" in data:
        out["application_description"] = data["ApplicationDescription"]
    if "Inputs" in data:
        import aws_sdk_kinesis_analytics.types.inputs

        out["inputs"] = aws_sdk_kinesis_analytics.types.inputs.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    if "Outputs" in data:
        import aws_sdk_kinesis_analytics.types.outputs

        out["outputs"] = (
            aws_sdk_kinesis_analytics.types.outputs.deserialize_aws_json_1_1(
                data["Outputs"]
            )
        )
    if "CloudWatchLoggingOptions" in data:
        import aws_sdk_kinesis_analytics.types.cloud_watch_logging_options

        out["cloud_watch_logging_options"] = (
            aws_sdk_kinesis_analytics.types.cloud_watch_logging_options.deserialize_aws_json_1_1(
                data["CloudWatchLoggingOptions"]
            )
        )
    if "ApplicationCode" in data:
        out["application_code"] = data["ApplicationCode"]
    if "Tags" in data:
        import aws_sdk_kinesis_analytics.types.tags

        out["tags"] = aws_sdk_kinesis_analytics.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
