"""Generated from Smithy shape ``com.amazonaws.macie2#__listOfDetectedDataDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_macie2.types.detected_data_details

__listOfDetectedDataDetails: TypeAlias = list[
    "aws_sdk_macie2.types.detected_data_details.DetectedDataDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfDetectedDataDetails) -> list:
    import aws_sdk_macie2.types.detected_data_details

    out: list = []
    for item in value:
        out.append(aws_sdk_macie2.types.detected_data_details.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfDetectedDataDetails:
    import aws_sdk_macie2.types.detected_data_details

    out: __listOfDetectedDataDetails = []
    for item in data:
        out.append(aws_sdk_macie2.types.detected_data_details.deserialize_json(item))
    return out
