"""Generated from Smithy shape ``com.amazonaws.rekognition#ChallengePreferences``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rekognition.types.challenge_preference

ChallengePreferences: TypeAlias = list[
    "capo_rekognition.types.challenge_preference.ChallengePreference"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ChallengePreferences) -> list:
    import capo_rekognition.types.challenge_preference

    out: list = []
    for item in value:
        out.append(
            capo_rekognition.types.challenge_preference.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ChallengePreferences:
    import capo_rekognition.types.challenge_preference

    out: ChallengePreferences = []
    for item in data:
        out.append(
            capo_rekognition.types.challenge_preference.deserialize_aws_json_1_1(item)
        )
    return out
