"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#SensitiveDataDetectionScope``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.sensitive_data_detection_scope_type

SensitiveDataDetectionScope: TypeAlias = list[
    "aws_sdk_bedrock_data_automation.types.sensitive_data_detection_scope_type.SensitiveDataDetectionScopeType"
]


# --- restJson1 ser/de ---
def serialize_json(value: SensitiveDataDetectionScope) -> list:
    import aws_sdk_bedrock_data_automation.types.sensitive_data_detection_scope_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_data_automation.types.sensitive_data_detection_scope_type.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SensitiveDataDetectionScope:
    import aws_sdk_bedrock_data_automation.types.sensitive_data_detection_scope_type

    out: SensitiveDataDetectionScope = []
    for item in data:
        out.append(
            aws_sdk_bedrock_data_automation.types.sensitive_data_detection_scope_type.deserialize_json(
                item
            )
        )
    return out
