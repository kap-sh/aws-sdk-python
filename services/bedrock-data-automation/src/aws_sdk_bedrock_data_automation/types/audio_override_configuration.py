"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#AudioOverrideConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.audio_language_configuration
    import aws_sdk_bedrock_data_automation.types.modality_processing_configuration
    import aws_sdk_bedrock_data_automation.types.sensitive_data_configuration


class AudioOverrideConfiguration(TypedDict, closed=True):
    modality_processing: NotRequired[
        "aws_sdk_bedrock_data_automation.types.modality_processing_configuration.ModalityProcessingConfiguration"
    ]
    language_configuration: NotRequired[
        "aws_sdk_bedrock_data_automation.types.audio_language_configuration.AudioLanguageConfiguration"
    ]
    sensitive_data_configuration: NotRequired[
        "aws_sdk_bedrock_data_automation.types.sensitive_data_configuration.SensitiveDataConfiguration"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: AudioOverrideConfiguration) -> dict:
    out: dict = {}
    if "modality_processing" in value:
        import aws_sdk_bedrock_data_automation.types.modality_processing_configuration

        out["modalityProcessing"] = (
            aws_sdk_bedrock_data_automation.types.modality_processing_configuration.serialize_json(
                value["modality_processing"]
            )
        )
    if "language_configuration" in value:
        import aws_sdk_bedrock_data_automation.types.audio_language_configuration

        out["languageConfiguration"] = (
            aws_sdk_bedrock_data_automation.types.audio_language_configuration.serialize_json(
                value["language_configuration"]
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


def deserialize_json(data: dict) -> AudioOverrideConfiguration:
    out: AudioOverrideConfiguration = {}  # type: ignore[typeddict-item]
    if "modalityProcessing" in data:
        import aws_sdk_bedrock_data_automation.types.modality_processing_configuration

        out["modality_processing"] = (
            aws_sdk_bedrock_data_automation.types.modality_processing_configuration.deserialize_json(
                data["modalityProcessing"]
            )
        )
    if "languageConfiguration" in data:
        import aws_sdk_bedrock_data_automation.types.audio_language_configuration

        out["language_configuration"] = (
            aws_sdk_bedrock_data_automation.types.audio_language_configuration.deserialize_json(
                data["languageConfiguration"]
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
