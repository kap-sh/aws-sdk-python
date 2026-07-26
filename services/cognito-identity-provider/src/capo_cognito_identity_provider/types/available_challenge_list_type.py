"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AvailableChallengeListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.challenge_name_type

AvailableChallengeListType: TypeAlias = list[
    "capo_cognito_identity_provider.types.challenge_name_type.ChallengeNameType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AvailableChallengeListType) -> list:
    import capo_cognito_identity_provider.types.challenge_name_type

    out: list = []
    for item in value:
        out.append(
            capo_cognito_identity_provider.types.challenge_name_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AvailableChallengeListType:
    import capo_cognito_identity_provider.types.challenge_name_type

    out: AvailableChallengeListType = []
    for item in data:
        out.append(
            capo_cognito_identity_provider.types.challenge_name_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
