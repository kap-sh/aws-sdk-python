"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#InputDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics.types.id
    import capo_kinesis_analytics.types.in_app_stream_name
    import capo_kinesis_analytics.types.in_app_stream_names
    import capo_kinesis_analytics.types.input_parallelism
    import capo_kinesis_analytics.types.input_processing_configuration_description
    import capo_kinesis_analytics.types.input_starting_position_configuration
    import capo_kinesis_analytics.types.kinesis_firehose_input_description
    import capo_kinesis_analytics.types.kinesis_streams_input_description
    import capo_kinesis_analytics.types.source_schema


class InputDescription(TypedDict, closed=True):
    input_id: NotRequired["capo_kinesis_analytics.types.id.Id"]
    """<p>Input ID associated with the application input. This is the ID that Amazon Kinesis Analytics assigns to each input configuration you add to your application. </p>"""
    name_prefix: NotRequired[
        "capo_kinesis_analytics.types.in_app_stream_name.InAppStreamName"
    ]
    """<p>In-application name prefix.</p>"""
    in_app_stream_names: NotRequired[
        "capo_kinesis_analytics.types.in_app_stream_names.InAppStreamNames"
    ]
    """<p>Returns the in-application stream names that are mapped to the stream source.</p>"""
    input_processing_configuration_description: NotRequired[
        "capo_kinesis_analytics.types.input_processing_configuration_description.InputProcessingConfigurationDescription"
    ]
    """<p>The description of the preprocessor that executes on records in this input before the application's code is run.</p>"""
    kinesis_streams_input_description: NotRequired[
        "capo_kinesis_analytics.types.kinesis_streams_input_description.KinesisStreamsInputDescription"
    ]
    """<p>If an Amazon Kinesis stream is configured as streaming source, provides Amazon Kinesis stream's Amazon Resource Name (ARN) and an IAM role that enables Amazon Kinesis Analytics to access the stream on your behalf.</p>"""
    kinesis_firehose_input_description: NotRequired[
        "capo_kinesis_analytics.types.kinesis_firehose_input_description.KinesisFirehoseInputDescription"
    ]
    """<p>If an Amazon Kinesis Firehose delivery stream is configured as a streaming source, provides the delivery stream's ARN and an IAM role that enables Amazon Kinesis Analytics to access the stream on your behalf.</p>"""
    input_schema: NotRequired["capo_kinesis_analytics.types.source_schema.SourceSchema"]
    """<p>Describes the format of the data in the streaming source, and how each data element maps to corresponding columns in the in-application stream that is being created. </p>"""
    input_parallelism: NotRequired[
        "capo_kinesis_analytics.types.input_parallelism.InputParallelism"
    ]
    """<p>Describes the configured parallelism (number of in-application streams mapped to the streaming source).</p>"""
    input_starting_position_configuration: NotRequired[
        "capo_kinesis_analytics.types.input_starting_position_configuration.InputStartingPositionConfiguration"
    ]
    """<p>Point at which the application is configured to read from the input stream.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputDescription) -> dict:
    out: dict = {}
    if "input_id" in value:
        out["InputId"] = value["input_id"]
    if "name_prefix" in value:
        out["NamePrefix"] = value["name_prefix"]
    if "in_app_stream_names" in value:
        import capo_kinesis_analytics.types.in_app_stream_names

        out["InAppStreamNames"] = (
            capo_kinesis_analytics.types.in_app_stream_names.serialize_aws_json_1_1(
                value["in_app_stream_names"]
            )
        )
    if "input_processing_configuration_description" in value:
        import capo_kinesis_analytics.types.input_processing_configuration_description

        out["InputProcessingConfigurationDescription"] = (
            capo_kinesis_analytics.types.input_processing_configuration_description.serialize_aws_json_1_1(
                value["input_processing_configuration_description"]
            )
        )
    if "kinesis_streams_input_description" in value:
        import capo_kinesis_analytics.types.kinesis_streams_input_description

        out["KinesisStreamsInputDescription"] = (
            capo_kinesis_analytics.types.kinesis_streams_input_description.serialize_aws_json_1_1(
                value["kinesis_streams_input_description"]
            )
        )
    if "kinesis_firehose_input_description" in value:
        import capo_kinesis_analytics.types.kinesis_firehose_input_description

        out["KinesisFirehoseInputDescription"] = (
            capo_kinesis_analytics.types.kinesis_firehose_input_description.serialize_aws_json_1_1(
                value["kinesis_firehose_input_description"]
            )
        )
    if "input_schema" in value:
        import capo_kinesis_analytics.types.source_schema

        out["InputSchema"] = (
            capo_kinesis_analytics.types.source_schema.serialize_aws_json_1_1(
                value["input_schema"]
            )
        )
    if "input_parallelism" in value:
        import capo_kinesis_analytics.types.input_parallelism

        out["InputParallelism"] = (
            capo_kinesis_analytics.types.input_parallelism.serialize_aws_json_1_1(
                value["input_parallelism"]
            )
        )
    if "input_starting_position_configuration" in value:
        import capo_kinesis_analytics.types.input_starting_position_configuration

        out["InputStartingPositionConfiguration"] = (
            capo_kinesis_analytics.types.input_starting_position_configuration.serialize_aws_json_1_1(
                value["input_starting_position_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InputDescription:
    out: InputDescription = {}  # type: ignore[typeddict-item]
    if "InputId" in data:
        out["input_id"] = data["InputId"]
    if "NamePrefix" in data:
        out["name_prefix"] = data["NamePrefix"]
    if "InAppStreamNames" in data:
        import capo_kinesis_analytics.types.in_app_stream_names

        out["in_app_stream_names"] = (
            capo_kinesis_analytics.types.in_app_stream_names.deserialize_aws_json_1_1(
                data["InAppStreamNames"]
            )
        )
    if "InputProcessingConfigurationDescription" in data:
        import capo_kinesis_analytics.types.input_processing_configuration_description

        out["input_processing_configuration_description"] = (
            capo_kinesis_analytics.types.input_processing_configuration_description.deserialize_aws_json_1_1(
                data["InputProcessingConfigurationDescription"]
            )
        )
    if "KinesisStreamsInputDescription" in data:
        import capo_kinesis_analytics.types.kinesis_streams_input_description

        out["kinesis_streams_input_description"] = (
            capo_kinesis_analytics.types.kinesis_streams_input_description.deserialize_aws_json_1_1(
                data["KinesisStreamsInputDescription"]
            )
        )
    if "KinesisFirehoseInputDescription" in data:
        import capo_kinesis_analytics.types.kinesis_firehose_input_description

        out["kinesis_firehose_input_description"] = (
            capo_kinesis_analytics.types.kinesis_firehose_input_description.deserialize_aws_json_1_1(
                data["KinesisFirehoseInputDescription"]
            )
        )
    if "InputSchema" in data:
        import capo_kinesis_analytics.types.source_schema

        out["input_schema"] = (
            capo_kinesis_analytics.types.source_schema.deserialize_aws_json_1_1(
                data["InputSchema"]
            )
        )
    if "InputParallelism" in data:
        import capo_kinesis_analytics.types.input_parallelism

        out["input_parallelism"] = (
            capo_kinesis_analytics.types.input_parallelism.deserialize_aws_json_1_1(
                data["InputParallelism"]
            )
        )
    if "InputStartingPositionConfiguration" in data:
        import capo_kinesis_analytics.types.input_starting_position_configuration

        out["input_starting_position_configuration"] = (
            capo_kinesis_analytics.types.input_starting_position_configuration.deserialize_aws_json_1_1(
                data["InputStartingPositionConfiguration"]
            )
        )
    return out
