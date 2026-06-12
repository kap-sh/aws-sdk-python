"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#InputDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.id
    import aws_sdk_kinesis_analytics_v2.types.in_app_stream_name
    import aws_sdk_kinesis_analytics_v2.types.in_app_stream_names
    import aws_sdk_kinesis_analytics_v2.types.input_parallelism
    import aws_sdk_kinesis_analytics_v2.types.input_processing_configuration_description
    import aws_sdk_kinesis_analytics_v2.types.input_starting_position_configuration
    import aws_sdk_kinesis_analytics_v2.types.kinesis_firehose_input_description
    import aws_sdk_kinesis_analytics_v2.types.kinesis_streams_input_description
    import aws_sdk_kinesis_analytics_v2.types.source_schema


class InputDescription(TypedDict):
    input_id: NotRequired["aws_sdk_kinesis_analytics_v2.types.id.Id"]
    """<p>The input ID that is associated with the application input. This is the ID that Kinesis Data Analytics assigns to each input configuration that you add to your application. </p>"""
    name_prefix: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.in_app_stream_name.InAppStreamName"
    ]
    """<p>The in-application name prefix.</p>"""
    in_app_stream_names: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.in_app_stream_names.InAppStreamNames"
    ]
    """<p>Returns the in-application stream names that are mapped to the stream source. </p>"""
    input_processing_configuration_description: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.input_processing_configuration_description.InputProcessingConfigurationDescription"
    ]
    """<p>The description of the preprocessor that executes on records in this input before the application's code is run. </p>"""
    kinesis_streams_input_description: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.kinesis_streams_input_description.KinesisStreamsInputDescription"
    ]
    """<p>If a Kinesis data stream is configured as a streaming source, provides the Kinesis data stream's Amazon Resource Name (ARN). </p>"""
    kinesis_firehose_input_description: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.kinesis_firehose_input_description.KinesisFirehoseInputDescription"
    ]
    """<p>If a Kinesis Data Firehose delivery stream is configured as a streaming source, provides the delivery stream's ARN. </p>"""
    input_schema: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.source_schema.SourceSchema"
    ]
    """<p>Describes the format of the data in the streaming source, and how each data element maps to corresponding columns in the in-application stream that is being created. </p>"""
    input_parallelism: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.input_parallelism.InputParallelism"
    ]
    """<p>Describes the configured parallelism (number of in-application streams mapped to the streaming source). </p>"""
    input_starting_position_configuration: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.input_starting_position_configuration.InputStartingPositionConfiguration"
    ]
    """<p>The point at which the application is configured to read from the input stream.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputDescription) -> dict:
    out: dict = {}
    if "input_id" in value:
        out["InputId"] = value["input_id"]
    if "name_prefix" in value:
        out["NamePrefix"] = value["name_prefix"]
    if "in_app_stream_names" in value:
        import aws_sdk_kinesis_analytics_v2.types.in_app_stream_names

        out["InAppStreamNames"] = (
            aws_sdk_kinesis_analytics_v2.types.in_app_stream_names.serialize_aws_json_1_1(
                value["in_app_stream_names"]
            )
        )
    if "input_processing_configuration_description" in value:
        import aws_sdk_kinesis_analytics_v2.types.input_processing_configuration_description

        out["InputProcessingConfigurationDescription"] = (
            aws_sdk_kinesis_analytics_v2.types.input_processing_configuration_description.serialize_aws_json_1_1(
                value["input_processing_configuration_description"]
            )
        )
    if "kinesis_streams_input_description" in value:
        import aws_sdk_kinesis_analytics_v2.types.kinesis_streams_input_description

        out["KinesisStreamsInputDescription"] = (
            aws_sdk_kinesis_analytics_v2.types.kinesis_streams_input_description.serialize_aws_json_1_1(
                value["kinesis_streams_input_description"]
            )
        )
    if "kinesis_firehose_input_description" in value:
        import aws_sdk_kinesis_analytics_v2.types.kinesis_firehose_input_description

        out["KinesisFirehoseInputDescription"] = (
            aws_sdk_kinesis_analytics_v2.types.kinesis_firehose_input_description.serialize_aws_json_1_1(
                value["kinesis_firehose_input_description"]
            )
        )
    if "input_schema" in value:
        import aws_sdk_kinesis_analytics_v2.types.source_schema

        out["InputSchema"] = (
            aws_sdk_kinesis_analytics_v2.types.source_schema.serialize_aws_json_1_1(
                value["input_schema"]
            )
        )
    if "input_parallelism" in value:
        import aws_sdk_kinesis_analytics_v2.types.input_parallelism

        out["InputParallelism"] = (
            aws_sdk_kinesis_analytics_v2.types.input_parallelism.serialize_aws_json_1_1(
                value["input_parallelism"]
            )
        )
    if "input_starting_position_configuration" in value:
        import aws_sdk_kinesis_analytics_v2.types.input_starting_position_configuration

        out["InputStartingPositionConfiguration"] = (
            aws_sdk_kinesis_analytics_v2.types.input_starting_position_configuration.serialize_aws_json_1_1(
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
        import aws_sdk_kinesis_analytics_v2.types.in_app_stream_names

        out["in_app_stream_names"] = (
            aws_sdk_kinesis_analytics_v2.types.in_app_stream_names.deserialize_aws_json_1_1(
                data["InAppStreamNames"]
            )
        )
    if "InputProcessingConfigurationDescription" in data:
        import aws_sdk_kinesis_analytics_v2.types.input_processing_configuration_description

        out["input_processing_configuration_description"] = (
            aws_sdk_kinesis_analytics_v2.types.input_processing_configuration_description.deserialize_aws_json_1_1(
                data["InputProcessingConfigurationDescription"]
            )
        )
    if "KinesisStreamsInputDescription" in data:
        import aws_sdk_kinesis_analytics_v2.types.kinesis_streams_input_description

        out["kinesis_streams_input_description"] = (
            aws_sdk_kinesis_analytics_v2.types.kinesis_streams_input_description.deserialize_aws_json_1_1(
                data["KinesisStreamsInputDescription"]
            )
        )
    if "KinesisFirehoseInputDescription" in data:
        import aws_sdk_kinesis_analytics_v2.types.kinesis_firehose_input_description

        out["kinesis_firehose_input_description"] = (
            aws_sdk_kinesis_analytics_v2.types.kinesis_firehose_input_description.deserialize_aws_json_1_1(
                data["KinesisFirehoseInputDescription"]
            )
        )
    if "InputSchema" in data:
        import aws_sdk_kinesis_analytics_v2.types.source_schema

        out["input_schema"] = (
            aws_sdk_kinesis_analytics_v2.types.source_schema.deserialize_aws_json_1_1(
                data["InputSchema"]
            )
        )
    if "InputParallelism" in data:
        import aws_sdk_kinesis_analytics_v2.types.input_parallelism

        out["input_parallelism"] = (
            aws_sdk_kinesis_analytics_v2.types.input_parallelism.deserialize_aws_json_1_1(
                data["InputParallelism"]
            )
        )
    if "InputStartingPositionConfiguration" in data:
        import aws_sdk_kinesis_analytics_v2.types.input_starting_position_configuration

        out["input_starting_position_configuration"] = (
            aws_sdk_kinesis_analytics_v2.types.input_starting_position_configuration.deserialize_aws_json_1_1(
                data["InputStartingPositionConfiguration"]
            )
        )
    return out
