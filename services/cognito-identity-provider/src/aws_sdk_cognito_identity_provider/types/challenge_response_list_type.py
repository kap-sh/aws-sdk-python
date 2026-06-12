"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ChallengeResponseListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.challenge_response_type

ChallengeResponseListType: TypeAlias = list[
    "aws_sdk_cognito_identity_provider.types.challenge_response_type.ChallengeResponseType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ChallengeResponseListType) -> list:
    import aws_sdk_cognito_identity_provider.types.challenge_response_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cognito_identity_provider.types.challenge_response_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ChallengeResponseListType:
    import aws_sdk_cognito_identity_provider.types.challenge_response_type

    out: ChallengeResponseListType = []
    for item in data:
        out.append(
            aws_sdk_cognito_identity_provider.types.challenge_response_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
