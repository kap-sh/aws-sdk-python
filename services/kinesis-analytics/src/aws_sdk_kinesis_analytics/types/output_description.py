"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#OutputDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics.types.destination_schema
    import aws_sdk_kinesis_analytics.types.id
    import aws_sdk_kinesis_analytics.types.in_app_stream_name
    import aws_sdk_kinesis_analytics.types.kinesis_firehose_output_description
    import aws_sdk_kinesis_analytics.types.kinesis_streams_output_description
    import aws_sdk_kinesis_analytics.types.lambda_output_description


class OutputDescription(TypedDict):
    output_id: NotRequired["aws_sdk_kinesis_analytics.types.id.Id"]
    """<p>A unique identifier for the output configuration.</p>"""
    name: NotRequired[
        "aws_sdk_kinesis_analytics.types.in_app_stream_name.InAppStreamName"
    ]
    """<p>Name of the in-application stream configured as output.</p>"""
    kinesis_streams_output_description: NotRequired[
        "aws_sdk_kinesis_analytics.types.kinesis_streams_output_description.KinesisStreamsOutputDescription"
    ]
    """<p>Describes Amazon Kinesis stream configured as the destination where output is written.</p>"""
    kinesis_firehose_output_description: NotRequired[
        "aws_sdk_kinesis_analytics.types.kinesis_firehose_output_description.KinesisFirehoseOutputDescription"
    ]
    """<p>Describes the Amazon Kinesis Firehose delivery stream configured as the destination where output is written.</p>"""
    lambda_output_description: NotRequired[
        "aws_sdk_kinesis_analytics.types.lambda_output_description.LambdaOutputDescription"
    ]
    """<p>Describes the AWS Lambda function configured as the destination where output is written.</p>"""
    destination_schema: NotRequired[
        "aws_sdk_kinesis_analytics.types.destination_schema.DestinationSchema"
    ]
    """<p>Data format used for writing data to the destination.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OutputDescription) -> dict:
    out: dict = {}
    if "output_id" in value:
        out["OutputId"] = value["output_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "kinesis_streams_output_description" in value:
        import aws_sdk_kinesis_analytics.types.kinesis_streams_output_description

        out["KinesisStreamsOutputDescription"] = (
            aws_sdk_kinesis_analytics.types.kinesis_streams_output_description.serialize_aws_json_1_1(
                value["kinesis_streams_output_description"]
            )
        )
    if "kinesis_firehose_output_description" in value:
        import aws_sdk_kinesis_analytics.types.kinesis_firehose_output_description

        out["KinesisFirehoseOutputDescription"] = (
            aws_sdk_kinesis_analytics.types.kinesis_firehose_output_description.serialize_aws_json_1_1(
                value["kinesis_firehose_output_description"]
            )
        )
    if "lambda_output_description" in value:
        import aws_sdk_kinesis_analytics.types.lambda_output_description

        out["LambdaOutputDescription"] = (
            aws_sdk_kinesis_analytics.types.lambda_output_description.serialize_aws_json_1_1(
                value["lambda_output_description"]
            )
        )
    if "destination_schema" in value:
        import aws_sdk_kinesis_analytics.types.destination_schema

        out["DestinationSchema"] = (
            aws_sdk_kinesis_analytics.types.destination_schema.serialize_aws_json_1_1(
                value["destination_schema"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OutputDescription:
    out: OutputDescription = {}  # type: ignore[typeddict-item]
    if "OutputId" in data:
        out["output_id"] = data["OutputId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "KinesisStreamsOutputDescription" in data:
        import aws_sdk_kinesis_analytics.types.kinesis_streams_output_description

        out["kinesis_streams_output_description"] = (
            aws_sdk_kinesis_analytics.types.kinesis_streams_output_description.deserialize_aws_json_1_1(
                data["KinesisStreamsOutputDescription"]
            )
        )
    if "KinesisFirehoseOutputDescription" in data:
        import aws_sdk_kinesis_analytics.types.kinesis_firehose_output_description

        out["kinesis_firehose_output_description"] = (
            aws_sdk_kinesis_analytics.types.kinesis_firehose_output_description.deserialize_aws_json_1_1(
                data["KinesisFirehoseOutputDescription"]
            )
        )
    if "LambdaOutputDescription" in data:
        import aws_sdk_kinesis_analytics.types.lambda_output_description

        out["lambda_output_description"] = (
            aws_sdk_kinesis_analytics.types.lambda_output_description.deserialize_aws_json_1_1(
                data["LambdaOutputDescription"]
            )
        )
    if "DestinationSchema" in data:
        import aws_sdk_kinesis_analytics.types.destination_schema

        out["destination_schema"] = (
            aws_sdk_kinesis_analytics.types.destination_schema.deserialize_aws_json_1_1(
                data["DestinationSchema"]
            )
        )
    return out
