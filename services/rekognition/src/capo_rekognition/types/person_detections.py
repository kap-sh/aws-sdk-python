"""Generated from Smithy shape ``com.amazonaws.rekognition#PersonDetections``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rekognition.types.person_detection

PersonDetections: TypeAlias = list[
    "capo_rekognition.types.person_detection.PersonDetection"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PersonDetections) -> list:
    import capo_rekognition.types.person_detection

    out: list = []
    for item in value:
        out.append(capo_rekognition.types.person_detection.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PersonDetections:
    import capo_rekognition.types.person_detection

    out: PersonDetections = []
    for item in data:
        out.append(
            capo_rekognition.types.person_detection.deserialize_aws_json_1_1(item)
        )
    return out
