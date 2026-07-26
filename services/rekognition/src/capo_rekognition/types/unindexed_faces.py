"""Generated from Smithy shape ``com.amazonaws.rekognition#UnindexedFaces``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rekognition.types.unindexed_face

UnindexedFaces: TypeAlias = list["capo_rekognition.types.unindexed_face.UnindexedFace"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnindexedFaces) -> list:
    import capo_rekognition.types.unindexed_face

    out: list = []
    for item in value:
        out.append(capo_rekognition.types.unindexed_face.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> UnindexedFaces:
    import capo_rekognition.types.unindexed_face

    out: UnindexedFaces = []
    for item in data:
        out.append(capo_rekognition.types.unindexed_face.deserialize_aws_json_1_1(item))
    return out
