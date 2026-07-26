"""Generated from Smithy shape ``com.amazonaws.rekognition#CelebrityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rekognition.types.celebrity

CelebrityList: TypeAlias = list["capo_rekognition.types.celebrity.Celebrity"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CelebrityList) -> list:
    import capo_rekognition.types.celebrity

    out: list = []
    for item in value:
        out.append(capo_rekognition.types.celebrity.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CelebrityList:
    import capo_rekognition.types.celebrity

    out: CelebrityList = []
    for item in data:
        out.append(capo_rekognition.types.celebrity.deserialize_aws_json_1_1(item))
    return out
