"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#AddApplicationInputProcessingConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.application_version_id
    import aws_sdk_kinesis_analytics_v2.types.id
    import aws_sdk_kinesis_analytics_v2.types.input_processing_configuration_description
    import aws_sdk_kinesis_analytics_v2.types.resource_arn


class AddApplicationInputProcessingConfigurationResponse(TypedDict, closed=True):
    application_arn: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.resource_arn.ResourceARN"
    ]
    """<p>The Amazon Resource Name (ARN) of the application.</p>"""
    application_version_id: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.application_version_id.ApplicationVersionId"
    ]
    """<p>Provides the current application version. </p>"""
    input_id: NotRequired["aws_sdk_kinesis_analytics_v2.types.id.Id"]
    """<p>The input ID that is associated with the application input. This is the ID that Kinesis Data Analytics assigns to each input configuration that you add to your application.</p>"""
    input_processing_configuration_description: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.input_processing_configuration_description.InputProcessingConfigurationDescription"
    ]
    """<p>The description of the preprocessor that executes on records in this input before the application's code is run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: AddApplicationInputProcessingConfigurationResponse,
) -> dict:
    out: dict = {}
    if "application_arn" in value:
        out["ApplicationARN"] = value["application_arn"]
    if "application_version_id" in value:
        out["ApplicationVersionId"] = value["application_version_id"]
    if "input_id" in value:
        out["InputId"] = value["input_id"]
    if "input_processing_configuration_description" in value:
        import aws_sdk_kinesis_analytics_v2.types.input_processing_configuration_description

        out["InputProcessingConfigurationDescription"] = (
            aws_sdk_kinesis_analytics_v2.types.input_processing_configuration_description.serialize_aws_json_1_1(
                value["input_processing_configuration_description"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> AddApplicationInputProcessingConfigurationResponse:
    out: AddApplicationInputProcessingConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "ApplicationARN" in data:
        out["application_arn"] = data["ApplicationARN"]
    if "ApplicationVersionId" in data:
        out["application_version_id"] = data["ApplicationVersionId"]
    if "InputId" in data:
        out["input_id"] = data["InputId"]
    if "InputProcessingConfigurationDescription" in data:
        import aws_sdk_kinesis_analytics_v2.types.input_processing_configuration_description

        out["input_processing_configuration_description"] = (
            aws_sdk_kinesis_analytics_v2.types.input_processing_configuration_description.deserialize_aws_json_1_1(
                data["InputProcessingConfigurationDescription"]
            )
        )
    return out
