"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DocumentOverrideConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.modality_processing_configuration
    import capo_bedrock_data_automation.types.sensitive_data_configuration
    import capo_bedrock_data_automation.types.splitter_configuration


class DocumentOverrideConfiguration(TypedDict, closed=True):
    splitter: NotRequired[
        "capo_bedrock_data_automation.types.splitter_configuration.SplitterConfiguration"
    ]
    modality_processing: NotRequired[
        "capo_bedrock_data_automation.types.modality_processing_configuration.ModalityProcessingConfiguration"
    ]
    sensitive_data_configuration: NotRequired[
        "capo_bedrock_data_automation.types.sensitive_data_configuration.SensitiveDataConfiguration"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentOverrideConfiguration) -> dict:
    out: dict = {}
    if "splitter" in value:
        import capo_bedrock_data_automation.types.splitter_configuration

        out["splitter"] = (
            capo_bedrock_data_automation.types.splitter_configuration.serialize_json(
                value["splitter"]
            )
        )
    if "modality_processing" in value:
        import capo_bedrock_data_automation.types.modality_processing_configuration

        out["modalityProcessing"] = (
            capo_bedrock_data_automation.types.modality_processing_configuration.serialize_json(
                value["modality_processing"]
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


def deserialize_json(data: dict) -> DocumentOverrideConfiguration:
    out: DocumentOverrideConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("splitter") is not None:
        import capo_bedrock_data_automation.types.splitter_configuration

        out["splitter"] = (
            capo_bedrock_data_automation.types.splitter_configuration.deserialize_json(
                data["splitter"]
            )
        )
    if data.get("modalityProcessing") is not None:
        import capo_bedrock_data_automation.types.modality_processing_configuration

        out["modality_processing"] = (
            capo_bedrock_data_automation.types.modality_processing_configuration.deserialize_json(
                data["modalityProcessing"]
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
