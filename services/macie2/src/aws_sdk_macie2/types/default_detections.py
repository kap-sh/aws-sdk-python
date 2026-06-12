"""Generated from Smithy shape ``com.amazonaws.macie2#DefaultDetections``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_macie2.types.default_detection

DefaultDetections: TypeAlias = list[
    "aws_sdk_macie2.types.default_detection.DefaultDetection"
]


# --- restJson1 ser/de ---
def serialize_json(value: DefaultDetections) -> list:
    import aws_sdk_macie2.types.default_detection

    out: list = []
    for item in value:
        out.append(aws_sdk_macie2.types.default_detection.serialize_json(item))
    return out


def deserialize_json(data: list) -> DefaultDetections:
    import aws_sdk_macie2.types.default_detection

    out: DefaultDetections = []
    for item in data:
        out.append(aws_sdk_macie2.types.default_detection.deserialize_json(item))
    return out
