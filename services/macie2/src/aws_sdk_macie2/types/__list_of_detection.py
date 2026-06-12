"""Generated from Smithy shape ``com.amazonaws.macie2#__listOfDetection``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_macie2.types.detection

__listOfDetection: TypeAlias = list["aws_sdk_macie2.types.detection.Detection"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfDetection) -> list:
    import aws_sdk_macie2.types.detection

    out: list = []
    for item in value:
        out.append(aws_sdk_macie2.types.detection.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfDetection:
    import aws_sdk_macie2.types.detection

    out: __listOfDetection = []
    for item in data:
        out.append(aws_sdk_macie2.types.detection.deserialize_json(item))
    return out
