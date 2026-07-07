"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#Input``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.in_app_stream_name
    import aws_sdk_kinesis_analytics_v2.types.input_parallelism
    import aws_sdk_kinesis_analytics_v2.types.input_processing_configuration
    import aws_sdk_kinesis_analytics_v2.types.kinesis_firehose_input
    import aws_sdk_kinesis_analytics_v2.types.kinesis_streams_input
    import aws_sdk_kinesis_analytics_v2.types.source_schema


class Input(TypedDict, closed=True):
    name_prefix: "aws_sdk_kinesis_analytics_v2.types.in_app_stream_name.InAppStreamName"
    r"""<p>The name prefix to use when creating an in-application stream. Suppose that you specify a prefix \"<code>MyInApplicationStream</code>.\" Kinesis Data Analytics then creates one or more (as per the <code>InputParallelism</code> count you specified) in-application streams with the names \"<code>MyInApplicationStream_001</code>,\" \"<code>MyInApplicationStream_002</code>,\" and so on. </p>"""
    input_processing_configuration: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.input_processing_configuration.InputProcessingConfiguration"
    ]
    """<p>The <a>InputProcessingConfiguration</a> for the input. An input processor transforms records as they are received from the stream, before the application's SQL code executes. Currently, the only input processing configuration available is <a>InputLambdaProcessor</a>. </p>"""
    kinesis_streams_input: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.kinesis_streams_input.KinesisStreamsInput"
    ]
    """<p>If the streaming source is an Amazon Kinesis data stream, identifies the stream's Amazon Resource Name (ARN). </p>"""
    kinesis_firehose_input: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.kinesis_firehose_input.KinesisFirehoseInput"
    ]
    """<p>If the streaming source is an Amazon Kinesis Data Firehose delivery stream, identifies the delivery stream's ARN.</p>"""
    input_parallelism: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.input_parallelism.InputParallelism"
    ]
    """<p>Describes the number of in-application streams to create. </p>"""
    input_schema: "aws_sdk_kinesis_analytics_v2.types.source_schema.SourceSchema"
    """<p>Describes the format of the data in the streaming source, and how each data element maps to corresponding columns in the in-application stream that is being created.</p> <p>Also used to describe the format of the reference data source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Input) -> dict:
    out: dict = {}
    out["NamePrefix"] = value["name_prefix"]
    if "input_processing_configuration" in value:
        import aws_sdk_kinesis_analytics_v2.types.input_processing_configuration

        out["InputProcessingConfiguration"] = (
            aws_sdk_kinesis_analytics_v2.types.input_processing_configuration.serialize_aws_json_1_1(
                value["input_processing_configuration"]
            )
        )
    if "kinesis_streams_input" in value:
        import aws_sdk_kinesis_analytics_v2.types.kinesis_streams_input

        out["KinesisStreamsInput"] = (
            aws_sdk_kinesis_analytics_v2.types.kinesis_streams_input.serialize_aws_json_1_1(
                value["kinesis_streams_input"]
            )
        )
    if "kinesis_firehose_input" in value:
        import aws_sdk_kinesis_analytics_v2.types.kinesis_firehose_input

        out["KinesisFirehoseInput"] = (
            aws_sdk_kinesis_analytics_v2.types.kinesis_firehose_input.serialize_aws_json_1_1(
                value["kinesis_firehose_input"]
            )
        )
    if "input_parallelism" in value:
        import aws_sdk_kinesis_analytics_v2.types.input_parallelism

        out["InputParallelism"] = (
            aws_sdk_kinesis_analytics_v2.types.input_parallelism.serialize_aws_json_1_1(
                value["input_parallelism"]
            )
        )
    import aws_sdk_kinesis_analytics_v2.types.source_schema

    out["InputSchema"] = (
        aws_sdk_kinesis_analytics_v2.types.source_schema.serialize_aws_json_1_1(
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
        import aws_sdk_kinesis_analytics_v2.types.input_processing_configuration

        out["input_processing_configuration"] = (
            aws_sdk_kinesis_analytics_v2.types.input_processing_configuration.deserialize_aws_json_1_1(
                data["InputProcessingConfiguration"]
            )
        )
    if "KinesisStreamsInput" in data:
        import aws_sdk_kinesis_analytics_v2.types.kinesis_streams_input

        out["kinesis_streams_input"] = (
            aws_sdk_kinesis_analytics_v2.types.kinesis_streams_input.deserialize_aws_json_1_1(
                data["KinesisStreamsInput"]
            )
        )
    if "KinesisFirehoseInput" in data:
        import aws_sdk_kinesis_analytics_v2.types.kinesis_firehose_input

        out["kinesis_firehose_input"] = (
            aws_sdk_kinesis_analytics_v2.types.kinesis_firehose_input.deserialize_aws_json_1_1(
                data["KinesisFirehoseInput"]
            )
        )
    if "InputParallelism" in data:
        import aws_sdk_kinesis_analytics_v2.types.input_parallelism

        out["input_parallelism"] = (
            aws_sdk_kinesis_analytics_v2.types.input_parallelism.deserialize_aws_json_1_1(
                data["InputParallelism"]
            )
        )
    if "InputSchema" in data:
        import aws_sdk_kinesis_analytics_v2.types.source_schema

        out["input_schema"] = (
            aws_sdk_kinesis_analytics_v2.types.source_schema.deserialize_aws_json_1_1(
                data["InputSchema"]
            )
        )
    else:
        raise DeserializationError("Input.input_schema required")
    return out
