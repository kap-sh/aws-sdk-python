"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#Output``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.destination_schema
    import aws_sdk_kinesis_analytics_v2.types.in_app_stream_name
    import aws_sdk_kinesis_analytics_v2.types.kinesis_firehose_output
    import aws_sdk_kinesis_analytics_v2.types.kinesis_streams_output
    import aws_sdk_kinesis_analytics_v2.types.lambda_output


class Output(TypedDict):
    name: "aws_sdk_kinesis_analytics_v2.types.in_app_stream_name.InAppStreamName"
    """<p>The name of the in-application stream.</p>"""
    kinesis_streams_output: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.kinesis_streams_output.KinesisStreamsOutput"
    ]
    """<p>Identifies a Kinesis data stream as the destination.</p>"""
    kinesis_firehose_output: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.kinesis_firehose_output.KinesisFirehoseOutput"
    ]
    """<p>Identifies a Kinesis Data Firehose delivery stream as the destination.</p>"""
    lambda_output: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.lambda_output.LambdaOutput"
    ]
    """<p>Identifies an Amazon Lambda function as the destination.</p>"""
    destination_schema: (
        "aws_sdk_kinesis_analytics_v2.types.destination_schema.DestinationSchema"
    )
    """<p>Describes the data format when records are written to the destination. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Output) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "kinesis_streams_output" in value:
        import aws_sdk_kinesis_analytics_v2.types.kinesis_streams_output

        out["KinesisStreamsOutput"] = (
            aws_sdk_kinesis_analytics_v2.types.kinesis_streams_output.serialize_aws_json_1_1(
                value["kinesis_streams_output"]
            )
        )
    if "kinesis_firehose_output" in value:
        import aws_sdk_kinesis_analytics_v2.types.kinesis_firehose_output

        out["KinesisFirehoseOutput"] = (
            aws_sdk_kinesis_analytics_v2.types.kinesis_firehose_output.serialize_aws_json_1_1(
                value["kinesis_firehose_output"]
            )
        )
    if "lambda_output" in value:
        import aws_sdk_kinesis_analytics_v2.types.lambda_output

        out["LambdaOutput"] = (
            aws_sdk_kinesis_analytics_v2.types.lambda_output.serialize_aws_json_1_1(
                value["lambda_output"]
            )
        )
    import aws_sdk_kinesis_analytics_v2.types.destination_schema

    out["DestinationSchema"] = (
        aws_sdk_kinesis_analytics_v2.types.destination_schema.serialize_aws_json_1_1(
            value["destination_schema"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> Output:
    out: Output = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("Output.name required")
    if "KinesisStreamsOutput" in data:
        import aws_sdk_kinesis_analytics_v2.types.kinesis_streams_output

        out["kinesis_streams_output"] = (
            aws_sdk_kinesis_analytics_v2.types.kinesis_streams_output.deserialize_aws_json_1_1(
                data["KinesisStreamsOutput"]
            )
        )
    if "KinesisFirehoseOutput" in data:
        import aws_sdk_kinesis_analytics_v2.types.kinesis_firehose_output

        out["kinesis_firehose_output"] = (
            aws_sdk_kinesis_analytics_v2.types.kinesis_firehose_output.deserialize_aws_json_1_1(
                data["KinesisFirehoseOutput"]
            )
        )
    if "LambdaOutput" in data:
        import aws_sdk_kinesis_analytics_v2.types.lambda_output

        out["lambda_output"] = (
            aws_sdk_kinesis_analytics_v2.types.lambda_output.deserialize_aws_json_1_1(
                data["LambdaOutput"]
            )
        )
    if "DestinationSchema" in data:
        import aws_sdk_kinesis_analytics_v2.types.destination_schema

        out["destination_schema"] = (
            aws_sdk_kinesis_analytics_v2.types.destination_schema.deserialize_aws_json_1_1(
                data["DestinationSchema"]
            )
        )
    else:
        raise DeserializationError("Output.destination_schema required")
    return out
