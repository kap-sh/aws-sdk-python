"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#GetTokensFromRefreshTokenResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.authentication_result_type


class GetTokensFromRefreshTokenResponse(TypedDict):
    authentication_result: NotRequired[
        "aws_sdk_cognito_identity_provider.types.authentication_result_type.AuthenticationResultType"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTokensFromRefreshTokenResponse) -> dict:
    out: dict = {}
    if "authentication_result" in value:
        import aws_sdk_cognito_identity_provider.types.authentication_result_type

        out["AuthenticationResult"] = (
            aws_sdk_cognito_identity_provider.types.authentication_result_type.serialize_aws_json_1_1(
                value["authentication_result"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTokensFromRefreshTokenResponse:
    out: GetTokensFromRefreshTokenResponse = {}  # type: ignore[typeddict-item]
    if "AuthenticationResult" in data:
        import aws_sdk_cognito_identity_provider.types.authentication_result_type

        out["authentication_result"] = (
            aws_sdk_cognito_identity_provider.types.authentication_result_type.deserialize_aws_json_1_1(
                data["AuthenticationResult"]
            )
        )
    return out
