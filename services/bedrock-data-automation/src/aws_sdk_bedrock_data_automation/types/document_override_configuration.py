"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DocumentOverrideConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.modality_processing_configuration
    import aws_sdk_bedrock_data_automation.types.sensitive_data_configuration
    import aws_sdk_bedrock_data_automation.types.splitter_configuration


class DocumentOverrideConfiguration(TypedDict):
    splitter: NotRequired[
        "aws_sdk_bedrock_data_automation.types.splitter_configuration.SplitterConfiguration"
    ]
    modality_processing: NotRequired[
        "aws_sdk_bedrock_data_automation.types.modality_processing_configuration.ModalityProcessingConfiguration"
    ]
    sensitive_data_configuration: NotRequired[
        "aws_sdk_bedrock_data_automation.types.sensitive_data_configuration.SensitiveDataConfiguration"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentOverrideConfiguration) -> dict:
    out: dict = {}
    if "splitter" in value:
        import aws_sdk_bedrock_data_automation.types.splitter_configuration

        out["splitter"] = (
            aws_sdk_bedrock_data_automation.types.splitter_configuration.serialize_json(
                value["splitter"]
            )
        )
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


def deserialize_json(data: dict) -> DocumentOverrideConfiguration:
    out: DocumentOverrideConfiguration = {}  # type: ignore[typeddict-item]
    if "splitter" in data:
        import aws_sdk_bedrock_data_automation.types.splitter_configuration

        out["splitter"] = (
            aws_sdk_bedrock_data_automation.types.splitter_configuration.deserialize_json(
                data["splitter"]
            )
        )
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
