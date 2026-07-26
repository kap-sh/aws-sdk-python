"""Generated from Smithy shape ``com.amazonaws.rekognition#ChallengeType``."""

from typing import Literal, TypeAlias, cast

ChallengeType: TypeAlias = Literal[
    "FaceMovementAndLightChallenge",
    "FaceMovementChallenge",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ChallengeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ChallengeType:
    return cast(ChallengeType, data)
