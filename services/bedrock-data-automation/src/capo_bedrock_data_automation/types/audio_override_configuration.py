"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#AudioOverrideConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.audio_language_configuration
    import capo_bedrock_data_automation.types.modality_processing_configuration
    import capo_bedrock_data_automation.types.sensitive_data_configuration


class AudioOverrideConfiguration(TypedDict, closed=True):
    modality_processing: NotRequired[
        "capo_bedrock_data_automation.types.modality_processing_configuration.ModalityProcessingConfiguration"
    ]
    language_configuration: NotRequired[
        "capo_bedrock_data_automation.types.audio_language_configuration.AudioLanguageConfiguration"
    ]
    sensitive_data_configuration: NotRequired[
        "capo_bedrock_data_automation.types.sensitive_data_configuration.SensitiveDataConfiguration"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: AudioOverrideConfiguration) -> dict:
    out: dict = {}
    if "modality_processing" in value:
        import capo_bedrock_data_automation.types.modality_processing_configuration

        out["modalityProcessing"] = (
            capo_bedrock_data_automation.types.modality_processing_configuration.serialize_json(
                value["modality_processing"]
            )
        )
    if "language_configuration" in value:
        import capo_bedrock_data_automation.types.audio_language_configuration

        out["languageConfiguration"] = (
            capo_bedrock_data_automation.types.audio_language_configuration.serialize_json(
                value["language_configuration"]
            )
        )
    if "sensitive_data_configuration" in value:
        import capo_bedrock_data_automation.types.sensitive_data_configuration

        out["sensitiveDataConfiguration"] = (
            capo_bedrock_data_automation.types.sensitive_data_configuration.serialize_json(
                value["sensitive_data_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> AudioOverrideConfiguration:
    out: AudioOverrideConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("modalityProcessing") is not None:
        import capo_bedrock_data_automation.types.modality_processing_configuration

        out["modality_processing"] = (
            capo_bedrock_data_automation.types.modality_processing_configuration.deserialize_json(
                data["modalityProcessing"]
            )
        )
    if data.get("languageConfiguration") is not None:
        import capo_bedrock_data_automation.types.audio_language_configuration

        out["language_configuration"] = (
            capo_bedrock_data_automation.types.audio_language_configuration.deserialize_json(
                data["languageConfiguration"]
            )
        )
    if data.get("sensitiveDataConfiguration") is not None:
        import capo_bedrock_data_automation.types.sensitive_data_configuration

        out["sensitive_data_configuration"] = (
            capo_bedrock_data_automation.types.sensitive_data_configuration.deserialize_json(
                data["sensitiveDataConfiguration"]
            )
        )
    return out
