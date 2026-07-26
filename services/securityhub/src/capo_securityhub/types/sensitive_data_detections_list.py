"""Generated from Smithy shape ``com.amazonaws.securityhub#SensitiveDataDetectionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.sensitive_data_detections

SensitiveDataDetectionsList: TypeAlias = list[
    "capo_securityhub.types.sensitive_data_detections.SensitiveDataDetections"
]


# --- restJson1 ser/de ---
def serialize_json(value: SensitiveDataDetectionsList) -> list:
    import capo_securityhub.types.sensitive_data_detections

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.sensitive_data_detections.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SensitiveDataDetectionsList:
    import capo_securityhub.types.sensitive_data_detections

    out: SensitiveDataDetectionsList = []
    for item in data:
        out.append(
            capo_securityhub.types.sensitive_data_detections.deserialize_json(item)
        )
    return out
