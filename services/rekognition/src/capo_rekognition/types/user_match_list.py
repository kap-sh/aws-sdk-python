"""Generated from Smithy shape ``com.amazonaws.rekognition#UserMatchList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rekognition.types.user_match

UserMatchList: TypeAlias = list["capo_rekognition.types.user_match.UserMatch"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserMatchList) -> list:
    import capo_rekognition.types.user_match

    out: list = []
    for item in value:
        out.append(capo_rekognition.types.user_match.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> UserMatchList:
    import capo_rekognition.types.user_match

    out: UserMatchList = []
    for item in data:
        out.append(capo_rekognition.types.user_match.deserialize_aws_json_1_1(item))
    return out
