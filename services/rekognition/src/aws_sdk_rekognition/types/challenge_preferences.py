"""Generated from Smithy shape ``com.amazonaws.rekognition#ChallengePreferences``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.challenge_preference

ChallengePreferences: TypeAlias = list[
    "aws_sdk_rekognition.types.challenge_preference.ChallengePreference"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ChallengePreferences) -> list:
    import aws_sdk_rekognition.types.challenge_preference

    out: list = []
    for item in value:
        out.append(
            aws_sdk_rekognition.types.challenge_preference.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ChallengePreferences:
    import aws_sdk_rekognition.types.challenge_preference

    out: ChallengePreferences = []
    for item in data:
        out.append(
            aws_sdk_rekognition.types.challenge_preference.deserialize_aws_json_1_1(
                item
            )
        )
    return out
