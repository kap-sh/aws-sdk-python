"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#SensitiveDataConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.pii_entities_configuration
    import aws_sdk_bedrock_data_automation.types.sensitive_data_detection_mode
    import aws_sdk_bedrock_data_automation.types.sensitive_data_detection_scope


class SensitiveDataConfiguration(TypedDict, closed=True):
    detection_mode: "aws_sdk_bedrock_data_automation.types.sensitive_data_detection_mode.SensitiveDataDetectionMode"
    """Mode for sensitive data detection"""
    detection_scope: NotRequired[
        "aws_sdk_bedrock_data_automation.types.sensitive_data_detection_scope.SensitiveDataDetectionScope"
    ]
    """Scope of detection - what types of sensitive data to detect"""
    pii_entities_configuration: NotRequired[
        "aws_sdk_bedrock_data_automation.types.pii_entities_configuration.PIIEntitiesConfiguration"
    ]
    """Configuration for PII entities detection and redaction"""


# --- restJson1 ser/de ---
def serialize_json(value: SensitiveDataConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_data_automation.types.sensitive_data_detection_mode

    out["detectionMode"] = (
        aws_sdk_bedrock_data_automation.types.sensitive_data_detection_mode.serialize_json(
            value["detection_mode"]
        )
    )
    if "detection_scope" in value:
        import aws_sdk_bedrock_data_automation.types.sensitive_data_detection_scope

        out["detectionScope"] = (
            aws_sdk_bedrock_data_automation.types.sensitive_data_detection_scope.serialize_json(
                value["detection_scope"]
            )
        )
    if "pii_entities_configuration" in value:
        import aws_sdk_bedrock_data_automation.types.pii_entities_configuration

        out["piiEntitiesConfiguration"] = (
            aws_sdk_bedrock_data_automation.types.pii_entities_configuration.serialize_json(
                value["pii_entities_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> SensitiveDataConfiguration:
    out: SensitiveDataConfiguration = {}  # type: ignore[typeddict-item]
    if "detectionMode" in data:
        import aws_sdk_bedrock_data_automation.types.sensitive_data_detection_mode

        out["detection_mode"] = (
            aws_sdk_bedrock_data_automation.types.sensitive_data_detection_mode.deserialize_json(
                data["detectionMode"]
            )
        )
    else:
        raise DeserializationError("SensitiveDataConfiguration.detection_mode required")
    if "detectionScope" in data:
        import aws_sdk_bedrock_data_automation.types.sensitive_data_detection_scope

        out["detection_scope"] = (
            aws_sdk_bedrock_data_automation.types.sensitive_data_detection_scope.deserialize_json(
                data["detectionScope"]
            )
        )
    if "piiEntitiesConfiguration" in data:
        import aws_sdk_bedrock_data_automation.types.pii_entities_configuration

        out["pii_entities_configuration"] = (
            aws_sdk_bedrock_data_automation.types.pii_entities_configuration.deserialize_json(
                data["piiEntitiesConfiguration"]
            )
        )
    return out
