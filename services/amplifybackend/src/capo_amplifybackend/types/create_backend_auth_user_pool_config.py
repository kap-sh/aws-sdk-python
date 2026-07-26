"""Generated from Smithy shape ``com.amazonaws.amplifybackend#CreateBackendAuthUserPoolConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifybackend.types.__string
    import capo_amplifybackend.types.create_backend_auth_forgot_password_config
    import capo_amplifybackend.types.create_backend_auth_mfa_config
    import capo_amplifybackend.types.create_backend_auth_o_auth_config
    import capo_amplifybackend.types.create_backend_auth_password_policy_config
    import capo_amplifybackend.types.create_backend_auth_verification_message_config
    import capo_amplifybackend.types.list_of_required_sign_up_attributes_element
    import capo_amplifybackend.types.sign_in_method


class CreateBackendAuthUserPoolConfig(TypedDict, closed=True):
    forgot_password: NotRequired[
        "capo_amplifybackend.types.create_backend_auth_forgot_password_config.CreateBackendAuthForgotPasswordConfig"
    ]
    """<p><b>(DEPRECATED)</b> Describes the forgotten password policy for your Amazon Cognito user pool, configured as a part of your Amplify project.</p>"""
    mfa: NotRequired[
        "capo_amplifybackend.types.create_backend_auth_mfa_config.CreateBackendAuthMFAConfig"
    ]
    """<p>Describes whether to apply multi-factor authentication policies for your Amazon Cognito user pool configured as a part of your Amplify project.</p>"""
    o_auth: NotRequired[
        "capo_amplifybackend.types.create_backend_auth_o_auth_config.CreateBackendAuthOAuthConfig"
    ]
    """<p>Describes the OAuth policy and rules for your Amazon Cognito user pool, configured as a part of your Amplify project.</p>"""
    password_policy: NotRequired[
        "capo_amplifybackend.types.create_backend_auth_password_policy_config.CreateBackendAuthPasswordPolicyConfig"
    ]
    """<p>Describes the password policy for your Amazon Cognito user pool, configured as a part of your Amplify project.</p>"""
    required_sign_up_attributes: NotRequired[
        "capo_amplifybackend.types.list_of_required_sign_up_attributes_element.ListOfRequiredSignUpAttributesElement"
    ]
    """<p>The required attributes to sign up new users in the user pool.</p>"""
    sign_in_method: NotRequired["capo_amplifybackend.types.sign_in_method.SignInMethod"]
    """<p>Describes the sign-in methods that your Amplify app users use to log in using the Amazon Cognito user pool, configured as a part of your Amplify project.</p>"""
    user_pool_name: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>The Amazon Cognito user pool name.</p>"""
    verification_message: NotRequired[
        "capo_amplifybackend.types.create_backend_auth_verification_message_config.CreateBackendAuthVerificationMessageConfig"
    ]
    """<p>Describes the email or SMS verification message for your Amazon Cognito user pool, configured as a part of your Amplify project.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBackendAuthUserPoolConfig) -> dict:
    out: dict = {}
    if "forgot_password" in value:
        import capo_amplifybackend.types.create_backend_auth_forgot_password_config

        out["forgotPassword"] = (
            capo_amplifybackend.types.create_backend_auth_forgot_password_config.serialize_json(
                value["forgot_password"]
            )
        )
    if "mfa" in value:
        import capo_amplifybackend.types.create_backend_auth_mfa_config

        out["mfa"] = (
            capo_amplifybackend.types.create_backend_auth_mfa_config.serialize_json(
                value["mfa"]
            )
        )
    if "o_auth" in value:
        import capo_amplifybackend.types.create_backend_auth_o_auth_config

        out["oAuth"] = (
            capo_amplifybackend.types.create_backend_auth_o_auth_config.serialize_json(
                value["o_auth"]
            )
        )
    if "password_policy" in value:
        import capo_amplifybackend.types.create_backend_auth_password_policy_config

        out["passwordPolicy"] = (
            capo_amplifybackend.types.create_backend_auth_password_policy_config.serialize_json(
                value["password_policy"]
            )
        )
    if "required_sign_up_attributes" in value:
        import capo_amplifybackend.types.list_of_required_sign_up_attributes_element

        out["requiredSignUpAttributes"] = (
            capo_amplifybackend.types.list_of_required_sign_up_attributes_element.serialize_json(
                value["required_sign_up_attributes"]
            )
        )
    if "sign_in_method" in value:
        import capo_amplifybackend.types.sign_in_method

        out["signInMethod"] = capo_amplifybackend.types.sign_in_method.serialize_json(
            value["sign_in_method"]
        )
    if "user_pool_name" in value:
        out["userPoolName"] = value["user_pool_name"]
    if "verification_message" in value:
        import capo_amplifybackend.types.create_backend_auth_verification_message_config

        out["verificationMessage"] = (
            capo_amplifybackend.types.create_backend_auth_verification_message_config.serialize_json(
                value["verification_message"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateBackendAuthUserPoolConfig:
    out: CreateBackendAuthUserPoolConfig = {}  # type: ignore[typeddict-item]
    if "forgotPassword" in data:
        import capo_amplifybackend.types.create_backend_auth_forgot_password_config

        out["forgot_password"] = (
            capo_amplifybackend.types.create_backend_auth_forgot_password_config.deserialize_json(
                data["forgotPassword"]
            )
        )
    if "mfa" in data:
        import capo_amplifybackend.types.create_backend_auth_mfa_config

        out["mfa"] = (
            capo_amplifybackend.types.create_backend_auth_mfa_config.deserialize_json(
                data["mfa"]
            )
        )
    if "oAuth" in data:
        import capo_amplifybackend.types.create_backend_auth_o_auth_config

        out["o_auth"] = (
            capo_amplifybackend.types.create_backend_auth_o_auth_config.deserialize_json(
                data["oAuth"]
            )
        )
    if "passwordPolicy" in data:
        import capo_amplifybackend.types.create_backend_auth_password_policy_config

        out["password_policy"] = (
            capo_amplifybackend.types.create_backend_auth_password_policy_config.deserialize_json(
                data["passwordPolicy"]
            )
        )
    if "requiredSignUpAttributes" in data:
        import capo_amplifybackend.types.list_of_required_sign_up_attributes_element

        out["required_sign_up_attributes"] = (
            capo_amplifybackend.types.list_of_required_sign_up_attributes_element.deserialize_json(
                data["requiredSignUpAttributes"]
            )
        )
    if "signInMethod" in data:
        import capo_amplifybackend.types.sign_in_method

        out["sign_in_method"] = (
            capo_amplifybackend.types.sign_in_method.deserialize_json(
                data["signInMethod"]
            )
        )
    if "userPoolName" in data:
        out["user_pool_name"] = data["userPoolName"]
    if "verificationMessage" in data:
        import capo_amplifybackend.types.create_backend_auth_verification_message_config

        out["verification_message"] = (
            capo_amplifybackend.types.create_backend_auth_verification_message_config.deserialize_json(
                data["verificationMessage"]
            )
        )
    return out
