"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#Input``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis_analytics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics.types.in_app_stream_name
    import aws_sdk_kinesis_analytics.types.input_parallelism
    import aws_sdk_kinesis_analytics.types.input_processing_configuration
    import aws_sdk_kinesis_analytics.types.kinesis_firehose_input
    import aws_sdk_kinesis_analytics.types.kinesis_streams_input
    import aws_sdk_kinesis_analytics.types.source_schema


class Input(TypedDict):
    name_prefix: "aws_sdk_kinesis_analytics.types.in_app_stream_name.InAppStreamName"
    r"""<p>Name prefix to use when creating an in-application stream. Suppose that you specify a prefix \"MyInApplicationStream.\" Amazon Kinesis Analytics then creates one or more (as per the <code>InputParallelism</code> count you specified) in-application streams with names \"MyInApplicationStream_001,\" \"MyInApplicationStream_002,\" and so on. </p>"""
    input_processing_configuration: NotRequired[
        "aws_sdk_kinesis_analytics.types.input_processing_configuration.InputProcessingConfiguration"
    ]
    r"""<p>The <a href=\"https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputProcessingConfiguration.html\">InputProcessingConfiguration</a> for the input. An input processor transforms records as they are received from the stream, before the application's SQL code executes. Currently, the only input processing configuration available is <a href=\"https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputLambdaProcessor.html\">InputLambdaProcessor</a>.</p>"""
    kinesis_streams_input: NotRequired[
        "aws_sdk_kinesis_analytics.types.kinesis_streams_input.KinesisStreamsInput"
    ]
    """<p>If the streaming source is an Amazon Kinesis stream, identifies the stream's Amazon Resource Name (ARN) and an IAM role that enables Amazon Kinesis Analytics to access the stream on your behalf.</p> <p>Note: Either <code>KinesisStreamsInput</code> or <code>KinesisFirehoseInput</code> is required.</p>"""
    kinesis_firehose_input: NotRequired[
        "aws_sdk_kinesis_analytics.types.kinesis_firehose_input.KinesisFirehoseInput"
    ]
    """<p>If the streaming source is an Amazon Kinesis Firehose delivery stream, identifies the delivery stream's ARN and an IAM role that enables Amazon Kinesis Analytics to access the stream on your behalf.</p> <p>Note: Either <code>KinesisStreamsInput</code> or <code>KinesisFirehoseInput</code> is required.</p>"""
    input_parallelism: NotRequired[
        "aws_sdk_kinesis_analytics.types.input_parallelism.InputParallelism"
    ]
    r"""<p>Describes the number of in-application streams to create. </p> <p>Data from your source is routed to these in-application input streams.</p> <p> (see <a href=\"https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-input.html\">Configuring Application Input</a>.</p>"""
    input_schema: "aws_sdk_kinesis_analytics.types.source_schema.SourceSchema"
    """<p>Describes the format of the data in the streaming source, and how each data element maps to corresponding columns in the in-application stream that is being created.</p> <p>Also used to describe the format of the reference data source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Input) -> dict:
    out: dict = {}
    out["NamePrefix"] = value["name_prefix"]
    if "input_processing_configuration" in value:
        import aws_sdk_kinesis_analytics.types.input_processing_configuration

        out["InputProcessingConfiguration"] = (
            aws_sdk_kinesis_analytics.types.input_processing_configuration.serialize_aws_json_1_1(
                value["input_processing_configuration"]
            )
        )
    if "kinesis_streams_input" in value:
        import aws_sdk_kinesis_analytics.types.kinesis_streams_input

        out["KinesisStreamsInput"] = (
            aws_sdk_kinesis_analytics.types.kinesis_streams_input.serialize_aws_json_1_1(
                value["kinesis_streams_input"]
            )
        )
    if "kinesis_firehose_input" in value:
        import aws_sdk_kinesis_analytics.types.kinesis_firehose_input

        out["KinesisFirehoseInput"] = (
            aws_sdk_kinesis_analytics.types.kinesis_firehose_input.serialize_aws_json_1_1(
                value["kinesis_firehose_input"]
            )
        )
    if "input_parallelism" in value:
        import aws_sdk_kinesis_analytics.types.input_parallelism

        out["InputParallelism"] = (
            aws_sdk_kinesis_analytics.types.input_parallelism.serialize_aws_json_1_1(
                value["input_parallelism"]
            )
        )
    import aws_sdk_kinesis_analytics.types.source_schema

    out["InputSchema"] = (
        aws_sdk_kinesis_analytics.types.source_schema.serialize_aws_json_1_1(
            value["input_schema"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> Input:
    out: Input = {}  # type: ignore[typeddict-item]
    if "NamePrefix" in data:
        out["name_prefix"] = data["NamePrefix"]
    else:
        raise DeserializationError("Input.name_prefix required")
    if "InputProcessingConfiguration" in data:
        import aws_sdk_kinesis_analytics.types.input_processing_configuration

        out["input_processing_configuration"] = (
            aws_sdk_kinesis_analytics.types.input_processing_configuration.deserialize_aws_json_1_1(
                data["InputProcessingConfiguration"]
            )
        )
    if "KinesisStreamsInput" in data:
        import aws_sdk_kinesis_analytics.types.kinesis_streams_input

        out["kinesis_streams_input"] = (
            aws_sdk_kinesis_analytics.types.kinesis_streams_input.deserialize_aws_json_1_1(
                data["KinesisStreamsInput"]
            )
        )
    if "KinesisFirehoseInput" in data:
        import aws_sdk_kinesis_analytics.types.kinesis_firehose_input

        out["kinesis_firehose_input"] = (
            aws_sdk_kinesis_analytics.types.kinesis_firehose_input.deserialize_aws_json_1_1(
                data["KinesisFirehoseInput"]
            )
        )
    if "InputParallelism" in data:
        import aws_sdk_kinesis_analytics.types.input_parallelism

        out["input_parallelism"] = (
            aws_sdk_kinesis_analytics.types.input_parallelism.deserialize_aws_json_1_1(
                data["InputParallelism"]
            )
        )
    if "InputSchema" in data:
        import aws_sdk_kinesis_analytics.types.source_schema

        out["input_schema"] = (
            aws_sdk_kinesis_analytics.types.source_schema.deserialize_aws_json_1_1(
                data["InputSchema"]
            )
        )
    else:
        raise DeserializationError("Input.input_schema required")
    return out
