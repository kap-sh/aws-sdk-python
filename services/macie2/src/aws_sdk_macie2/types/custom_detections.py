"""Generated from Smithy shape ``com.amazonaws.macie2#CustomDetections``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_macie2.types.custom_detection

CustomDetections: TypeAlias = list[
    "aws_sdk_macie2.types.custom_detection.CustomDetection"
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomDetections) -> list:
    import aws_sdk_macie2.types.custom_detection

    out: list = []
    for item in value:
        out.append(aws_sdk_macie2.types.custom_detection.serialize_json(item))
    return out


def deserialize_json(data: list) -> CustomDetections:
    import aws_sdk_macie2.types.custom_detection

    out: CustomDetections = []
    for item in data:
        out.append(aws_sdk_macie2.types.custom_detection.deserialize_json(item))
    return out
