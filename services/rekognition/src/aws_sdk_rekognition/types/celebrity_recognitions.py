"""Generated from Smithy shape ``com.amazonaws.rekognition#CelebrityRecognitions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.celebrity_recognition

CelebrityRecognitions: TypeAlias = list[
    "aws_sdk_rekognition.types.celebrity_recognition.CelebrityRecognition"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CelebrityRecognitions) -> list:
    import aws_sdk_rekognition.types.celebrity_recognition

    out: list = []
    for item in value:
        out.append(
            aws_sdk_rekognition.types.celebrity_recognition.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CelebrityRecognitions:
    import aws_sdk_rekognition.types.celebrity_recognition

    out: CelebrityRecognitions = []
    for item in data:
        out.append(
            aws_sdk_rekognition.types.celebrity_recognition.deserialize_aws_json_1_1(
                item
            )
        )
    return out
