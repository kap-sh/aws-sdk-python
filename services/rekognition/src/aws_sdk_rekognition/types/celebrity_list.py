"""Generated from Smithy shape ``com.amazonaws.rekognition#CelebrityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.celebrity

CelebrityList: TypeAlias = list["aws_sdk_rekognition.types.celebrity.Celebrity"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CelebrityList) -> list:
    import aws_sdk_rekognition.types.celebrity

    out: list = []
    for item in value:
        out.append(aws_sdk_rekognition.types.celebrity.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CelebrityList:
    import aws_sdk_rekognition.types.celebrity

    out: CelebrityList = []
    for item in data:
        out.append(aws_sdk_rekognition.types.celebrity.deserialize_aws_json_1_1(item))
    return out
