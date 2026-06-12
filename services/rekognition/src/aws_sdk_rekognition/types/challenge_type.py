"""Generated from Smithy shape ``com.amazonaws.rekognition#ChallengeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rekognition.errors import DeserializationError

ChallengeType: TypeAlias = Literal[
    "FaceMovementAndLightChallenge",
    "FaceMovementChallenge",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FaceMovementAndLightChallenge",
        "FaceMovementChallenge",
    )
)


def serialize_aws_json_1_1(value: ChallengeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ChallengeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChallengeType value: {data!r}")
    return cast(ChallengeType, data)
