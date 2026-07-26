"""Generated from Smithy shape ``com.amazonaws.rekognition#UnsearchedFaceReasons``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rekognition.types.unsearched_face_reason

UnsearchedFaceReasons: TypeAlias = list[
    "capo_rekognition.types.unsearched_face_reason.UnsearchedFaceReason"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnsearchedFaceReasons) -> list:
    import capo_rekognition.types.unsearched_face_reason

    out: list = []
    for item in value:
        out.append(
            capo_rekognition.types.unsearched_face_reason.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UnsearchedFaceReasons:
    import capo_rekognition.types.unsearched_face_reason

    out: UnsearchedFaceReasons = []
    for item in data:
        out.append(
            capo_rekognition.types.unsearched_face_reason.deserialize_aws_json_1_1(item)
        )
    return out
