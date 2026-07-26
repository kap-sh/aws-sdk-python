"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ChallengeResponseType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.challenge_name
    import capo_cognito_identity_provider.types.challenge_response


class ChallengeResponseType(TypedDict, closed=True):
    challenge_name: NotRequired[
        "capo_cognito_identity_provider.types.challenge_name.ChallengeName"
    ]
    """<p>The type of challenge that your previous authentication request returned in the parameter <code>ChallengeName</code>, for example <code>SMS_MFA</code>.</p>"""
    challenge_response: NotRequired[
        "capo_cognito_identity_provider.types.challenge_response.ChallengeResponse"
    ]
    """<p>The set of key-value pairs that provides a response to the requested challenge.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ChallengeResponseType) -> dict:
    out: dict = {}
    if "challenge_name" in value:
        import capo_cognito_identity_provider.types.challenge_name

        out["ChallengeName"] = (
            capo_cognito_identity_provider.types.challenge_name.serialize_aws_json_1_1(
                value["challenge_name"]
            )
        )
    if "challenge_response" in value:
        import capo_cognito_identity_provider.types.challenge_response

        out["ChallengeResponse"] = (
            capo_cognito_identity_provider.types.challenge_response.serialize_aws_json_1_1(
                value["challenge_response"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ChallengeResponseType:
    out: ChallengeResponseType = {}  # type: ignore[typeddict-item]
    if "ChallengeName" in data:
        import capo_cognito_identity_provider.types.challenge_name

        out["challenge_name"] = (
            capo_cognito_identity_provider.types.challenge_name.deserialize_aws_json_1_1(
                data["ChallengeName"]
            )
        )
    if "ChallengeResponse" in data:
        import capo_cognito_identity_provider.types.challenge_response

        out["challenge_response"] = (
            capo_cognito_identity_provider.types.challenge_response.deserialize_aws_json_1_1(
                data["ChallengeResponse"]
            )
        )
    return out
