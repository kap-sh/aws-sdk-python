"""Generated from Smithy shape ``com.amazonaws.rekognition#CompareFacesMatchList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.compare_faces_match

CompareFacesMatchList: TypeAlias = list[
    "aws_sdk_rekognition.types.compare_faces_match.CompareFacesMatch"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CompareFacesMatchList) -> list:
    import aws_sdk_rekognition.types.compare_faces_match

    out: list = []
    for item in value:
        out.append(
            aws_sdk_rekognition.types.compare_faces_match.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CompareFacesMatchList:
    import aws_sdk_rekognition.types.compare_faces_match

    out: CompareFacesMatchList = []
    for item in data:
        out.append(
            aws_sdk_rekognition.types.compare_faces_match.deserialize_aws_json_1_1(item)
        )
    return out
