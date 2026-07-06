"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#AddApplicationOutputRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_kinesis_analytics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics.types.application_name
    import aws_sdk_kinesis_analytics.types.application_version_id
    import aws_sdk_kinesis_analytics.types.output


class AddApplicationOutputRequest(TypedDict, closed=True):
    application_name: "aws_sdk_kinesis_analytics.types.application_name.ApplicationName"
    """<p>Name of the application to which you want to add the output configuration.</p>"""
    current_application_version_id: (
        "aws_sdk_kinesis_analytics.types.application_version_id.ApplicationVersionId"
    )
    r"""<p>Version of the application to which you want to add the output configuration. You can use the <a href=\"https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html\">DescribeApplication</a> operation to get the current application version. If the version specified is not the current version, the <code>ConcurrentModificationException</code> is returned. </p>"""
    output: "aws_sdk_kinesis_analytics.types.output.Output"
    """<p>An array of objects, each describing one output configuration. In the output configuration, you specify the name of an in-application stream, a destination (that is, an Amazon Kinesis stream, an Amazon Kinesis Firehose delivery stream, or an AWS Lambda function), and record the formation to use when writing to the destination.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddApplicationOutputRequest) -> dict:
    out: dict = {}
    out["ApplicationName"] = value["application_name"]
    out["CurrentApplicationVersionId"] = value["current_application_version_id"]
    import aws_sdk_kinesis_analytics.types.output

    out["Output"] = aws_sdk_kinesis_analytics.types.output.serialize_aws_json_1_1(
        value["output"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AddApplicationOutputRequest:
    out: AddApplicationOutputRequest = {}  # type: ignore[typeddict-item]
    if "ApplicationName" in data:
        out["application_name"] = data["ApplicationName"]
    else:
        raise DeserializationError(
            "AddApplicationOutputRequest.application_name required"
        )
    if "CurrentApplicationVersionId" in data:
        out["current_application_version_id"] = data["CurrentApplicationVersionId"]
    else:
        raise DeserializationError(
            "AddApplicationOutputRequest.current_application_version_id required"
        )
    if "Output" in data:
        import aws_sdk_kinesis_analytics.types.output

        out["output"] = aws_sdk_kinesis_analytics.types.output.deserialize_aws_json_1_1(
            data["Output"]
        )
    else:
        raise DeserializationError("AddApplicationOutputRequest.output required")
    return out
