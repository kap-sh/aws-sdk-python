"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#DiscoverInputSchemaRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.input_processing_configuration
    import aws_sdk_kinesis_analytics_v2.types.input_starting_position_configuration
    import aws_sdk_kinesis_analytics_v2.types.resource_arn
    import aws_sdk_kinesis_analytics_v2.types.role_arn
    import aws_sdk_kinesis_analytics_v2.types.s3_configuration


class DiscoverInputSchemaRequest(TypedDict, closed=True):
    resource_arn: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.resource_arn.ResourceARN"
    ]
    """<p>The Amazon Resource Name (ARN) of the streaming source.</p>"""
    service_execution_role: "aws_sdk_kinesis_analytics_v2.types.role_arn.RoleARN"
    """<p>The ARN of the role that is used to access the streaming source.</p>"""
    input_starting_position_configuration: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.input_starting_position_configuration.InputStartingPositionConfiguration"
    ]
    """<p>The point at which you want Kinesis Data Analytics to start reading records from the specified streaming source for discovery purposes.</p>"""
    s3_configuration: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.s3_configuration.S3Configuration"
    ]
    """<p>Specify this parameter to discover a schema from data in an Amazon S3 object.</p>"""
    input_processing_configuration: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.input_processing_configuration.InputProcessingConfiguration"
    ]
    """<p>The <a>InputProcessingConfiguration</a> to use to preprocess the records before discovering the schema of the records.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DiscoverInputSchemaRequest) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceARN"] = value["resource_arn"]
    out["ServiceExecutionRole"] = value["service_execution_role"]
    if "input_starting_position_configuration" in value:
        import aws_sdk_kinesis_analytics_v2.types.input_starting_position_configuration

        out["InputStartingPositionConfiguration"] = (
            aws_sdk_kinesis_analytics_v2.types.input_starting_position_configuration.serialize_aws_json_1_1(
                value["input_starting_position_configuration"]
            )
        )
    if "s3_configuration" in value:
        import aws_sdk_kinesis_analytics_v2.types.s3_configuration

        out["S3Configuration"] = (
            aws_sdk_kinesis_analytics_v2.types.s3_configuration.serialize_aws_json_1_1(
                value["s3_configuration"]
            )
        )
    if "input_processing_configuration" in value:
        import aws_sdk_kinesis_analytics_v2.types.input_processing_configuration

        out["InputProcessingConfiguration"] = (
            aws_sdk_kinesis_analytics_v2.types.input_processing_configuration.serialize_aws_json_1_1(
                value["input_processing_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DiscoverInputSchemaRequest:
    out: DiscoverInputSchemaRequest = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    if "ServiceExecutionRole" in data:
        out["service_execution_role"] = data["ServiceExecutionRole"]
    else:
        raise DeserializationError(
            "DiscoverInputSchemaRequest.service_execution_role required"
        )
    if "InputStartingPositionConfiguration" in data:
        import aws_sdk_kinesis_analytics_v2.types.input_starting_position_configuration

        out["input_starting_position_configuration"] = (
            aws_sdk_kinesis_analytics_v2.types.input_starting_position_configuration.deserialize_aws_json_1_1(
                data["InputStartingPositionConfiguration"]
            )
        )
    if "S3Configuration" in data:
        import aws_sdk_kinesis_analytics_v2.types.s3_configuration

        out["s3_configuration"] = (
            aws_sdk_kinesis_analytics_v2.types.s3_configuration.deserialize_aws_json_1_1(
                data["S3Configuration"]
            )
        )
    if "InputProcessingConfiguration" in data:
        import aws_sdk_kinesis_analytics_v2.types.input_processing_configuration

        out["input_processing_configuration"] = (
            aws_sdk_kinesis_analytics_v2.types.input_processing_configuration.deserialize_aws_json_1_1(
                data["InputProcessingConfiguration"]
            )
        )
    return out
