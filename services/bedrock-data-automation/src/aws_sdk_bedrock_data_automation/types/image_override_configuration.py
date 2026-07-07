"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#ImageOverrideConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.modality_processing_configuration
    import aws_sdk_bedrock_data_automation.types.sensitive_data_configuration


class ImageOverrideConfiguration(TypedDict, closed=True):
    modality_processing: NotRequired[
        "aws_sdk_bedrock_data_automation.types.modality_processing_configuration.ModalityProcessingConfiguration"
    ]
    sensitive_data_configuration: NotRequired[
        "aws_sdk_bedrock_data_automation.types.sensitive_data_configuration.SensitiveDataConfiguration"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ImageOverrideConfiguration) -> dict:
    out: dict = {}
    if "modality_processing" in value:
        import aws_sdk_bedrock_data_automation.types.modality_processing_configuration

        out["modalityProcessing"] = (
            aws_sdk_bedrock_data_automation.types.modality_processing_configuration.serialize_json(
                value["modality_processing"]
            )
        )
    if "sensitive_data_configuration" in value:
        import aws_sdk_bedrock_data_automation.types.sensitive_data_configuration

        out["sensitiveDataConfiguration"] = (
            aws_sdk_bedrock_data_automation.types.sensitive_data_configuration.serialize_json(
                value["sensitive_data_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ImageOverrideConfiguration:
    out: ImageOverrideConfiguration = {}  # type: ignore[typeddict-item]
    if "modalityProcessing" in data:
        import aws_sdk_bedrock_data_automation.types.modality_processing_configuration

        out["modality_processing"] = (
            aws_sdk_bedrock_data_automation.types.modality_processing_configuration.deserialize_json(
                data["modalityProcessing"]
            )
        )
    if "sensitiveDataConfiguration" in data:
        import aws_sdk_bedrock_data_automation.types.sensitive_data_configuration

        out["sensitive_data_configuration"] = (
            aws_sdk_bedrock_data_automation.types.sensitive_data_configuration.deserialize_json(
                data["sensitiveDataConfiguration"]
            )
        )
    return out
