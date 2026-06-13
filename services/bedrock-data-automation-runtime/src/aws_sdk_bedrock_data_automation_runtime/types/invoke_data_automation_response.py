"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#InvokeDataAutomationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_data_automation_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation_runtime.types.output_configuration
    import aws_sdk_bedrock_data_automation_runtime.types.output_segment_list
    import aws_sdk_bedrock_data_automation_runtime.types.semantic_modality


class InvokeDataAutomationResponse(TypedDict):
    output_configuration: NotRequired[
        "aws_sdk_bedrock_data_automation_runtime.types.output_configuration.OutputConfiguration"
    ]
    """Output configuration"""
    semantic_modality: "aws_sdk_bedrock_data_automation_runtime.types.semantic_modality.SemanticModality"
    """Detected semantic modality"""
    output_segments: "aws_sdk_bedrock_data_automation_runtime.types.output_segment_list.OutputSegmentList"
    """List of outputs for each logical sub-doc"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvokeDataAutomationResponse) -> dict:
    out: dict = {}
    if "output_configuration" in value:
        import aws_sdk_bedrock_data_automation_runtime.types.output_configuration

        out["outputConfiguration"] = (
            aws_sdk_bedrock_data_automation_runtime.types.output_configuration.serialize_aws_json_1_1(
                value["output_configuration"]
            )
        )
    import aws_sdk_bedrock_data_automation_runtime.types.semantic_modality

    out["semanticModality"] = (
        aws_sdk_bedrock_data_automation_runtime.types.semantic_modality.serialize_aws_json_1_1(
            value["semantic_modality"]
        )
    )
    import aws_sdk_bedrock_data_automation_runtime.types.output_segment_list

    out["outputSegments"] = (
        aws_sdk_bedrock_data_automation_runtime.types.output_segment_list.serialize_aws_json_1_1(
            value.get("output_segments", [])
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> InvokeDataAutomationResponse:
    out: InvokeDataAutomationResponse = {}  # type: ignore[typeddict-item]
    if "outputConfiguration" in data:
        import aws_sdk_bedrock_data_automation_runtime.types.output_configuration

        out["output_configuration"] = (
            aws_sdk_bedrock_data_automation_runtime.types.output_configuration.deserialize_aws_json_1_1(
                data["outputConfiguration"]
            )
        )
    if "semanticModality" in data:
        import aws_sdk_bedrock_data_automation_runtime.types.semantic_modality

        out["semantic_modality"] = (
            aws_sdk_bedrock_data_automation_runtime.types.semantic_modality.deserialize_aws_json_1_1(
                data["semanticModality"]
            )
        )
    else:
        raise DeserializationError(
            "InvokeDataAutomationResponse.semantic_modality required"
        )
    if "outputSegments" in data:
        import aws_sdk_bedrock_data_automation_runtime.types.output_segment_list

        out["output_segments"] = (
            aws_sdk_bedrock_data_automation_runtime.types.output_segment_list.deserialize_aws_json_1_1(
                data["outputSegments"]
            )
        )
    else:
        out["output_segments"] = []
    return out
