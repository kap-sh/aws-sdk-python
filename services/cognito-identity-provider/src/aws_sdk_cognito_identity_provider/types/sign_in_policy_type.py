"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#SignInPolicyType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.allowed_first_auth_factors_list_type


class SignInPolicyType(TypedDict, closed=True):
    allowed_first_auth_factors: NotRequired[
        "aws_sdk_cognito_identity_provider.types.allowed_first_auth_factors_list_type.AllowedFirstAuthFactorsListType"
    ]
    """<p>The sign-in methods that a user pool supports as the first factor. You can permit users to start authentication with a standard username and password, or with other one-time password and hardware factors.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SignInPolicyType) -> dict:
    out: dict = {}
    if "allowed_first_auth_factors" in value:
        import aws_sdk_cognito_identity_provider.types.allowed_first_auth_factors_list_type

        out["AllowedFirstAuthFactors"] = (
            aws_sdk_cognito_identity_provider.types.allowed_first_auth_factors_list_type.serialize_aws_json_1_1(
                value["allowed_first_auth_factors"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SignInPolicyType:
    out: SignInPolicyType = {}  # type: ignore[typeddict-item]
    if "AllowedFirstAuthFactors" in data:
        import aws_sdk_cognito_identity_provider.types.allowed_first_auth_factors_list_type

        out["allowed_first_auth_factors"] = (
            aws_sdk_cognito_identity_provider.types.allowed_first_auth_factors_list_type.deserialize_aws_json_1_1(
                data["AllowedFirstAuthFactors"]
            )
        )
    return out
