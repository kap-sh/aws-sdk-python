"""Generated from Smithy shape ``com.amazonaws.securityhub#CustomDataIdentifiersDetectionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.custom_data_identifiers_detections

CustomDataIdentifiersDetectionsList: TypeAlias = list[
    "aws_sdk_securityhub.types.custom_data_identifiers_detections.CustomDataIdentifiersDetections"
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomDataIdentifiersDetectionsList) -> list:
    import aws_sdk_securityhub.types.custom_data_identifiers_detections

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.custom_data_identifiers_detections.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CustomDataIdentifiersDetectionsList:
    import aws_sdk_securityhub.types.custom_data_identifiers_detections

    out: CustomDataIdentifiersDetectionsList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.custom_data_identifiers_detections.deserialize_json(
                item
            )
        )
    return out
