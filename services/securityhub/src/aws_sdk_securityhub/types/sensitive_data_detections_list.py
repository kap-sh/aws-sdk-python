"""Generated from Smithy shape ``com.amazonaws.securityhub#SensitiveDataDetectionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.sensitive_data_detections

SensitiveDataDetectionsList: TypeAlias = list[
    "aws_sdk_securityhub.types.sensitive_data_detections.SensitiveDataDetections"
]


# --- restJson1 ser/de ---
def serialize_json(value: SensitiveDataDetectionsList) -> list:
    import aws_sdk_securityhub.types.sensitive_data_detections

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.sensitive_data_detections.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SensitiveDataDetectionsList:
    import aws_sdk_securityhub.types.sensitive_data_detections

    out: SensitiveDataDetectionsList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.sensitive_data_detections.deserialize_json(item)
        )
    return out
