"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UserPoolPolicyType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.password_policy_type
    import capo_cognito_identity_provider.types.sign_in_policy_type


class UserPoolPolicyType(TypedDict, closed=True):
    password_policy: NotRequired[
        "capo_cognito_identity_provider.types.password_policy_type.PasswordPolicyType"
    ]
    """<p>The password policy settings for a user pool, including complexity, history, and length requirements.</p>"""
    sign_in_policy: NotRequired[
        "capo_cognito_identity_provider.types.sign_in_policy_type.SignInPolicyType"
    ]
    """<p>The policy for allowed types of authentication in a user pool.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserPoolPolicyType) -> dict:
    out: dict = {}
    if "password_policy" in value:
        import capo_cognito_identity_provider.types.password_policy_type

        out["PasswordPolicy"] = (
            capo_cognito_identity_provider.types.password_policy_type.serialize_aws_json_1_1(
                value["password_policy"]
            )
        )
    if "sign_in_policy" in value:
        import capo_cognito_identity_provider.types.sign_in_policy_type

        out["SignInPolicy"] = (
            capo_cognito_identity_provider.types.sign_in_policy_type.serialize_aws_json_1_1(
                value["sign_in_policy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UserPoolPolicyType:
    out: UserPoolPolicyType = {}  # type: ignore[typeddict-item]
    if "PasswordPolicy" in data:
        import capo_cognito_identity_provider.types.password_policy_type

        out["password_policy"] = (
            capo_cognito_identity_provider.types.password_policy_type.deserialize_aws_json_1_1(
                data["PasswordPolicy"]
            )
        )
    if "SignInPolicy" in data:
        import capo_cognito_identity_provider.types.sign_in_policy_type

        out["sign_in_policy"] = (
            capo_cognito_identity_provider.types.sign_in_policy_type.deserialize_aws_json_1_1(
                data["SignInPolicy"]
            )
        )
    return out
